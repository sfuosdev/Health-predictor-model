import argparse
import re
from pathlib import Path

import pandas as pd

# By default, Pandas assumes the first row of a CSV
# contains the column headers. We use df.columns as input.
def clean_headers(column_headers: pd.Index) -> list[str]:
    """
    Cleans column headers by converting them to snake_case
    and ensuring all names are unique.
    """
    cleaned_headers = []
    # Tracks previously used header names.
    used = set()

    # Standardizes column headers into snake_case.
    for col in column_headers:
        name = str(col).strip().lower()
        name = re.sub(r"[^a-z0-9]+", "_", name)
        name = name.strip("_") or "unnamed"

        # Prevents duplicate column header names.
        base = name
        counter = 1

        while name in used:
            name = f"{base}_{counter}"
            counter += 1

        cleaned_headers.append(name)
        used.add(name)

    return cleaned_headers


def clean_data(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    """Normalize formatting, remove duplicates, and flag invalid predictors."""

    # Work on a copy so the original dataset stays unchanged for reporting.
    cleaned_df = df.copy()
    original_headers = list(cleaned_df.columns)

    # Standardize headers and count which names were changed.
    cleaned_headers = clean_headers(cleaned_df.columns)
    cleaned_df.columns = cleaned_headers
    headers_standardized = sum(
        str(original) != cleaned
        for original, cleaned in zip(original_headers, cleaned_headers)
    )

    # Trim surrounding whitespace in text cells before checking duplicates.
    formatting_cells_trimmed = 0
    text_columns = cleaned_df.select_dtypes(include=["object", "string"]).columns
    for column in text_columns:
        original_values = cleaned_df[column]
        trimmed_values = original_values.map(
            lambda value: value.strip() if isinstance(value, str) else value
        )
        formatting_cells_trimmed += int(
            (original_values.notna() & original_values.ne(trimmed_values)).sum()
        )
        cleaned_df[column] = trimmed_values

    # Check that all columns needed for this CVD dataset are present.
    required_columns = {
        "id", "age", "gender", "height", "weight", "ap_hi", "ap_lo",
        "cholesterol", "gluc", "smoke", "alco", "active", "cardio",
    }
    missing_columns = required_columns.difference(cleaned_df.columns)
    if missing_columns:
        raise ValueError(
            f"Dataset is missing required columns: {sorted(missing_columns)}"
        )

    # Record the starting row and ID counts for the before/after report.
    id_count_before = int(
        pd.to_numeric(cleaned_df["id"], errors="coerce").nunique()
    )
    rows_before = len(cleaned_df)

    # Remove exact duplicate rows before checking individual fields.
    duplicates_removed = int(cleaned_df.duplicated().sum())
    cleaned_df = cleaned_df.drop_duplicates().copy()

    # Convert expected numeric fields and remember values that could not parse.
    numeric_columns = [
        "id", "age", "gender", "height", "weight", "ap_hi", "ap_lo",
        "cholesterol", "gluc", "smoke", "alco", "active", "cardio",
    ]
    parse_errors = {}
    for column in numeric_columns:
        original_values = cleaned_df[column]
        numeric_values = pd.to_numeric(original_values, errors="coerce")
        parse_errors[column] = original_values.notna() & numeric_values.isna()
        cleaned_df[column] = numeric_values

    # Identify absent, non-numeric, or non-integer IDs and invalid targets.
    id_invalid = (
        cleaned_df["id"].isna()
        | parse_errors["id"]
        | (cleaned_df["id"] % 1 != 0)
    )
    target_invalid = (
        cleaned_df["cardio"].isna()
        | parse_errors["cardio"]
        | ~cleaned_df["cardio"].isin([0, 1])
    )

    # Find repeated IDs that have different row contents.
    duplicate_ids = (
        ~id_invalid
        & cleaned_df["id"].duplicated(keep=False)
    )

    # Set the allowed values for coded category and binary columns.
    allowed_categories = {
        "gender": [1, 2],
        "cholesterol": [1, 2, 3],
        "gluc": [1, 2, 3],
        "smoke": [0, 1],
        "alco": [0, 1],
        "active": [0, 1],
    }
    invalid_predictors = {}

    # Flag category values outside their documented codes.
    for column, allowed_values in allowed_categories.items():
        invalid_predictors[column] = (
            parse_errors[column]
            | (
                cleaned_df[column].notna()
                & ~cleaned_df[column].isin(allowed_values)
            )
        )

    age = cleaned_df["age"]
    height = cleaned_df["height"]
    weight = cleaned_df["weight"]
    systolic = cleaned_df["ap_hi"]
    diastolic = cleaned_df["ap_lo"]

    # Flag measurements outside the broad plausible value ranges.
    invalid_predictors["age"] = (
        parse_errors["age"]
        | (age.notna() & ~age.between(0, 120 * 365.25))
    )
    invalid_predictors["height"] = (
        parse_errors["height"]
        | (height.notna() & ~height.between(100, 250))
    )
    invalid_predictors["weight"] = (
        parse_errors["weight"]
        | (weight.notna() & ~weight.between(20, 350))
    )

    # Check systolic and diastolic pressure ranges separately.
    invalid_systolic = (
        parse_errors["ap_hi"]
        | (systolic.notna() & ~systolic.between(60, 300))
    )
    invalid_diastolic = (
        parse_errors["ap_lo"]
        | (diastolic.notna() & ~diastolic.between(30, 200))
    )

    # Flag an invalid pressure order only when both values pass range checks.
    invalid_bp_order = (
        systolic.notna()
        & diastolic.notna()
        & (systolic <= diastolic)
        & ~invalid_systolic
        & ~invalid_diastolic
    )

    # Treat a bad reading or pressure order as one invalid predictor group.
    invalid_predictors["blood_pressure"] = (
        invalid_systolic | invalid_diastolic | invalid_bp_order
    )

    # Count suspect predictor cells before removing rows or setting values aside.
    suspect_values_detected = sum(
        int(mask.sum())
        for column, mask in invalid_predictors.items()
        if column != "blood_pressure"
    )
    suspect_values_detected += int(
        (invalid_systolic | invalid_bp_order).sum()
    )
    suspect_values_detected += int(
        (invalid_diastolic | invalid_bp_order).sum()
    )

    # Remove rows that cannot be trusted as identified, labeled records.
    rows_with_invalid_id = int(id_invalid.sum())
    rows_with_invalid_target = int(target_invalid.sum())
    rows_with_duplicate_ids = int(duplicate_ids.sum())
    invalid_record_mask = id_invalid | target_invalid | duplicate_ids

    # Remove rows with suspect values in two or more predictor groups.
    suspect_group_count = pd.DataFrame(
        invalid_predictors, index=cleaned_df.index
    ).sum(axis=1)
    multiple_suspect_groups_mask = (
        (suspect_group_count >= 2) & ~invalid_record_mask
    )
    rows_with_multiple_suspect_groups_removed = int(
        multiple_suspect_groups_mask.sum()
    )
    rows_to_keep = ~(invalid_record_mask | multiple_suspect_groups_mask)
    cleaned_df = cleaned_df.loc[rows_to_keep].copy()

    # Set isolated invalid category values aside for later imputation.
    suspect_values_set_aside = 0
    for column in allowed_categories:
        invalid_mask = invalid_predictors[column].loc[cleaned_df.index]
        suspect_values_set_aside += int(invalid_mask.sum())
        cleaned_df.loc[invalid_mask, column] = float("nan")

    # Set isolated invalid continuous measurements aside as well.
    for column in ("age", "height", "weight"):
        invalid_mask = invalid_predictors[column].loc[cleaned_df.index]
        suspect_values_set_aside += int(invalid_mask.sum())
        cleaned_df.loc[invalid_mask, column] = float("nan")

    # Set suspect pressure values aside rather than guessing a replacement.
    invalid_systolic = invalid_systolic.loc[cleaned_df.index]
    invalid_diastolic = invalid_diastolic.loc[cleaned_df.index]
    invalid_bp_order = invalid_bp_order.loc[cleaned_df.index]
    suspect_values_set_aside += int(
        (invalid_systolic | invalid_bp_order).sum()
    )
    suspect_values_set_aside += int(
        (invalid_diastolic | invalid_bp_order).sum()
    )
    cleaned_df.loc[invalid_systolic | invalid_bp_order, "ap_hi"] = float("nan")
    cleaned_df.loc[invalid_diastolic | invalid_bp_order, "ap_lo"] = float("nan")

    # Keep ID and coded category columns as integers while allowing NaN values.
    for column in (
        "id", "gender", "cholesterol", "gluc", "smoke", "alco", "active",
        "cardio",
    ):
        cleaned_df[column] = cleaned_df[column].astype("Int64")

    # Return the cleaned data and counts used by the results report.
    summary = {
        "rows_before": rows_before,
        "rows_after": len(cleaned_df),
        "duplicates_removed": duplicates_removed,
        "invalid_id_rows_removed": rows_with_invalid_id,
        "invalid_target_rows_removed": rows_with_invalid_target,
        "duplicate_id_rows_removed": rows_with_duplicate_ids,
        "rows_with_multiple_suspect_groups_removed":
            rows_with_multiple_suspect_groups_removed,
        "suspect_values_detected": suspect_values_detected,
        "suspect_values_set_aside": suspect_values_set_aside,
        "invalid_predictor_rows": {
            column: int(mask.sum())
            for column, mask in invalid_predictors.items()
        },
        "headers_standardized": headers_standardized,
        "formatting_cells_trimmed": formatting_cells_trimmed,
        "id_count_before": id_count_before,
        "id_count_after": int(cleaned_df["id"].nunique()),
    }
    return cleaned_df, summary


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Automated CSV data cleaning tool"
    )

    parser.add_argument(
        "--member",
        required=True,
        help="Member name, e.g. firstname-lastname"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Input CSV file path"
    )

    return parser.parse_args()

def validate_member(member: str) -> None:
    """Validates the member name for safe output paths."""

    if not re.fullmatch(r"[a-zA-Z0-9_-]+", member):
        raise ValueError(
            "Invalid member name. Use letters, numbers, - or _."
        )

def resolve_paths(input_file: str, member: str) -> tuple[Path, Path]:
    """Resolves input and output file paths."""
    resolved_file = Path(__file__).resolve()
    project_root = (
        resolved_file.parents[2]
        if len(resolved_file.parents) > 2
        else resolved_file.parent
    )

    input_path = Path(input_file).expanduser()
    if not input_path.is_absolute():
        input_path = (Path.cwd() / input_path).resolve()

    output_path = (
        project_root
        / "data"
        / "processed"
        / member
        / "cleaned_dataset.csv"
    )

    return input_path, output_path

def load_dataset(input_path: Path) -> pd.DataFrame:
    """Validates and loads the input CSV dataset."""

    if not input_path.is_file():
        raise FileNotFoundError(
            f"Input file not found: {input_path}"
        )

    print(f"\nLoading: {input_path}")

    return pd.read_csv(input_path, sep=None, engine="python", dtype=str)

def report_results(
    original_df: pd.DataFrame,
    cleaned_df: pd.DataFrame,
    dataset_name: str,
    summary: dict
) -> None:
    """
    Generates a report comparing the original and cleaned datasets.
    """

    # Calculate before and after metrics.
    before_rows = len(original_df)
    after_rows = len(cleaned_df)
    before_suspect_values = summary["suspect_values_detected"]
    after_suspect_values = summary["suspect_values_set_aside"]
    blank_input_cells = original_df.isna().sum().sum()
    before_duplicates = original_df.duplicated().sum()
    after_duplicates = cleaned_df.duplicated().sum()
    formatting_before = (
        summary["headers_standardized"] + summary["formatting_cells_trimmed"]
    )

    # Display dataset information.
    print("\n========== DATASET INFORMATION ==========")
    print(f"Dataset Name: {dataset_name}")
    print(f"Number of Rows: {before_rows} before, {after_rows} after")
    print(f"Number of Columns: {len(cleaned_df.columns)}")

    print("\n========== DATA QUALITY ISSUES FOUND ==========")
    print(
        f"Suspect values: {before_suspect_values} before, "
        f"{after_suspect_values} set aside after"
    )
    print(f"Blank input cells: {blank_input_cells}")
    print(f"Duplicate rows: {before_duplicates} before, {after_duplicates} after")
    print(f"Invalid ID rows removed: {summary['invalid_id_rows_removed']}")
    print(f"Invalid target rows removed: {summary['invalid_target_rows_removed']}")
    print(f"Duplicate-ID rows removed: {summary['duplicate_id_rows_removed']}")
    print(
        "Rows removed for suspect values in 2+ predictor groups: "
        f"{summary['rows_with_multiple_suspect_groups_removed']}"
    )
    print(
        "Suspect predictor values set aside for train-only imputation: "
        f"{summary['suspect_values_set_aside']}"
    )
    print("Suspect predictor rows flagged by group before row removal:")
    for column, count in summary["invalid_predictor_rows"].items():
        if count:
            print(f"  {column}: {count}")
    if not any(summary["invalid_predictor_rows"].values()):
        print("  None")
    print(
        "Column headers standardized: "
        f"{summary['headers_standardized']}"
    )
    print(
        "Text cells trimmed: "
        f"{summary['formatting_cells_trimmed']}"
    )
    print(f"Unique IDs: {summary['id_count_before']} before")
    print(f"Unique IDs: {summary['id_count_after']} after")

    # Display before and after comparison.
    print("\n========== BEFORE & AFTER SUMMARY ==========")
    print(f"{'Metric':<20}{'Before':<15}{'After':<15}")
    print("-" * 50)

    print(f"{'Rows':<20}{before_rows:<15}{after_rows:<15}")
    print(
        f"{'Suspect Values':<20}{before_suspect_values:<15}"
        f"{after_suspect_values:<15}"
    )
    print(f"{'Duplicates':<20}{before_duplicates:<15}{after_duplicates:<15}")
    print(
        f"{'Format issues':<20}{formatting_before:<15}{0:<15}"
    )

    # Display cleaning methods and results.
    print("\n========== CLEANING SUMMARY ==========")
    print(f"Duplicates removed: {summary['duplicates_removed']}")
    print(f"Output: {summary.get('output_path', 'See output location')}")
    print("Imputation: deferred until after train/test split")

    print("============================================\n")

def main():
    # Parse command-line arguments provided by the user
    args = parse_arguments()

    # Validate the member name before using it in output paths
    validate_member(args.member)

    # Determine the input file location and output destination.
    input_path, output_path = resolve_paths(args.input, args.member)

    df = load_dataset(input_path)
    print("Cleaning dataset...")
    cleaned_df, summary = clean_data(df)

    # Create the output directory if it doesn't already exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Display the cleaning results and output file location
    cleaned_df.to_csv(output_path, index=False)

    summary["output_path"] = str(output_path)

    report_results(
        original_df=df,
        cleaned_df=cleaned_df,
        dataset_name=input_path.name,
        summary=summary
    )

if __name__ == "__main__":
    main()