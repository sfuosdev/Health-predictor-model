"""Clean and validate the UCI Cleveland Heart Disease dataset.

Place processed.cleveland.data in data/raw/moksha-dilip/.

Run from the repository root:
    python3 src/data_cleaning/moksha-dilip-clean.py --member moksha-dilip --input processed.cleveland.data

The script supplies column names for the headerless .data file,
standardizes missing markers, validates numeric values and category
codes, checks duplicates, and counts potential outliers.

Outputs are saved in data/processed/moksha-dilip/.
"""

import argparse
import csv
import json
import math
from pathlib import Path
from statistics import quantiles


# TASK: Add required column names, including the prediction target.
REQUIRED_COLUMNS = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num",
]

# TASK: Add missing markers ONLY after checking the dataset documentation.
# For example, "NA" can be a real category in some datasets.
MISSING_MARKERS = {"", "?"}
ALLOWED_CODES = {
    "sex": {0, 1},
    "cp": {1, 2, 3, 4},
    "fbs": {0, 1},
    "restecg": {0, 1, 2},
    "exang": {0, 1},
    "slope": {1, 2, 3},
    "ca": {0, 1, 2, 3},
    "thal": {3, 6, 7},
    "num": {0, 1, 2, 3, 4},
}


def clean_value(column, value):
    value = value.strip()
    if value in MISSING_MARKERS:
        return ""

    try:
        number = float(value)
    except ValueError:
        raise ValueError(f"{column}: expected a number, got {value!r}") from None

    if not math.isfinite(number):
        raise ValueError(f"{column}: expected a finite number, got {value!r}")

    allowed = ALLOWED_CODES.get(column)
    if allowed is not None and number not in allowed:
        raise ValueError(
            f"{column}: expected one of {sorted(allowed)}, got {value!r}"
        )

    return value


def summarize(rows, columns):
    """Count extra copies of exact rows, not all members of duplicate groups."""
    seen = set()
    duplicates = 0
    missing = 0
    for row in rows:
        key = tuple(row[column] for column in columns)
        duplicates += key in seen
        seen.add(key)
        missing += sum(value.strip() in MISSING_MARKERS for value in key)
    return {"rows": len(rows), "columns": len(columns),
            "missing_values": missing, "duplicate_rows": duplicates}


def clean_data(rows, columns, remove_duplicates=False):
    """Return new records and comparable before/after quality counts."""
    before = summarize(rows, columns)
    cleaned = []
    seen = set()
    duplicates_removed = 0
    for row in rows:
        cleaned_row = {
            column: clean_value(column, row[column]) for column in columns
        }
        # Convert results back to text because CSV stores text, not Python types.
        cleaned_row = {
            column: "" if value is None else str(value)
            for column, value in cleaned_row.items()
        }
        key = tuple(cleaned_row[column] for column in columns)
        if remove_duplicates and key in seen:
            duplicates_removed += 1
            continue
        seen.add(key)
        cleaned.append(cleaned_row)
    return cleaned, {
        "before": before,
        "after": summarize(cleaned, columns),
        "duplicates_removed_after_normalization": duplicates_removed,
        "remove_duplicates": remove_duplicates,
        "missing_markers": sorted(MISSING_MARKERS),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--member", required=True, help="firstname-lastname")
    parser.add_argument("--input", required=True,
                        help="CSV filename inside data/raw/<member>/")
    parser.add_argument("--delimiter", default=",", help="Default: comma")
    parser.add_argument("--encoding", default="utf-8-sig")
    parser.add_argument("--remove-duplicates", action="store_true",
                        help="Use only when duplicate removal is justified")
    args = parser.parse_args()

    if not args.member or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-"
                              for c in args.member):
        parser.error("Use lowercase letters, numbers, and hyphens for --member.")
    if len(args.delimiter) != 1:
        parser.error("--delimiter must be one character.")

    # Locate the repository from this script, not a machine-specific path.
    root = Path(__file__).resolve().parents[2]
    raw_dir = (root / "data" / "raw" / args.member).resolve()
    source = (raw_dir / args.input).resolve()
    if source.parent != raw_dir or source.suffix.lower() not in {".csv", ".data"}:
        parser.error("--input must be a .csv or .data file inside your raw folder.")
    if not source.is_file():
        parser.error(f"Input CSV not found: {source}")

    with source.open(encoding=args.encoding, newline="") as handle:
        reader = csv.DictReader(
            handle,
            fieldnames=REQUIRED_COLUMNS if source.suffix.lower() == ".data" else None,
            delimiter=args.delimiter,
            strict=True,
        )
        columns = reader.fieldnames
        if not columns or any(not name.strip() for name in columns):
            parser.error("The CSV needs a header with nonempty column names.")
        if len(set(columns)) != len(columns):
            parser.error("Duplicate column names found. Resolve them first.")
        absent = [name for name in REQUIRED_COLUMNS if name not in columns]
        if absent:
            parser.error(f"Required columns missing: {absent}")
        rows = []
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                parser.error(f"Wrong number of fields near CSV line {reader.line_num}.")
            rows.append(row)
    if not rows:
        parser.error("The CSV has no data records.")

    cleaned, summary = clean_data(rows, columns, args.remove_duplicates)
    outliers = {}
    for column in ("age", "trestbps", "chol", "thalach", "oldpeak"):
        values = [float(row[column]) for row in cleaned if row[column] != ""]
        if len(values) < 2:
            continue
        q1, _, q3 = quantiles(values, n=4, method="inclusive")
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers[column] = sum(value < lower or value > upper for value in values)
    summary["potential_outliers"] = outliers
    output_dir = root / "data" / "processed" / args.member
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{source.stem}_cleaned.csv"
    summary_file = output_dir / f"{source.stem}_summary.json"
    # Re-running updates these generated outputs; the raw input is never written.
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=args.delimiter)
        writer.writeheader()
        writer.writerows(cleaned)
    summary["input"] = str(source.relative_to(root))
    summary["output"] = str(output.relative_to(root))
    summary_file.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print(f"Saved CSV: {output}")
    print(f"Saved summary: {summary_file}")
    print("Complete your cleaning report with decisions and remaining issues.")


if __name__ == "__main__":
    main()
