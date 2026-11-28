# Cardiovascular Dataset Cleaning Report

## Dataset

- **Input dataset:** `data/raw/hendrick-custodio/dataset_1_sulianova/cardio_train.csv`
- **Rows:** 70,000 rows before cleaning
- **Columns:** 13 columns before cleaning

## Data Quality Issues Found

- **Suspect values:** 1,471 detected; 1,463 set aside for later imputation.
  The input had no blank cells.
- **Duplicate rows:** 0 exact duplicates; 0 duplicate IDs.
- **Rows removed for multiple suspect measurements:** 4 rows had suspect values
  in at least two predictor groups. Systolic and diastolic pressure together
  count as one group. No rows were removed for invalid IDs, target values, or
  duplicate IDs, and no invalid category codes were found.
- **Outliers:** No statistical outlier test is performed. Values outside
  documented plausibility checks are counted as suspect values.
- **Formatting inconsistencies:** 0 headers standardized and 0 text cells
  trimmed for surrounding whitespace.

## Cleaning approach

1. Standardize column headers and trim surrounding whitespace from text cells,
   then remove exact duplicate rows.
2. Validate that the expected CVD columns exist. Check IDs and the `cardio`
   target, and remove rows with absent/invalid IDs, invalid targets, or
   conflicting duplicate IDs. Do not invent IDs or target labels.
3. Validate coded fields: `gender` must be 1/2; `cholesterol` and `gluc` must
   be 1–3; `smoke`, `alco`, `active`, and `cardio` must be 0/1.
4. Apply conservative plausibility checks to continuous predictors:
   - Age: 0–120 years, converted from the source's days.
   - Height: 100–250 cm.
   - Weight: 20–350 kg.
   - Systolic pressure (`ap_hi`): 60–300; diastolic pressure (`ap_lo`): 30–200.
     Systolic pressure must also be greater than diastolic pressure.
5. Set isolated suspect predictor measurements aside as NaN. Remove a row only
   when it has suspect values in at least two distinct predictor groups
   (for example, height and blood pressure). The two blood pressure readings
   count together as one group. Do not remove or cap valid values solely
   because they are statistically unusual.
6. Leave suspect predictor values as NaN for imputation after the train/test
   split. Fit imputation values on training data only to avoid data leakage.
   Keep `id` as an identifier, not as a model feature.

The broad ranges above are data-quality screens, not clinical cutoffs. Extreme
but valid measurements are retained when they fall within the checks.


## Summary of changes

- **Changed:** Standardized headers and whitespace, checked duplicates and
  invalid values, and set isolated suspect measurements aside.
- **Why:** Improve consistency and avoid keeping records with issues across
  multiple predictor groups.
- **Assumptions:** Broad measurement ranges are quality checks, not clinical
  limits; blood pressure readings count as one predictor group.


## Before and after

| Metric | Before | After |
|---|---:|---:|
| Rows | 70,000 | 69,996 |
| Blank input cells | 0 | 0 |
| Duplicate rows | 0 | 0 |
| Suspect values | 1,471 | 1,463 |

`Before` counts suspect predictor cells across all 70,000 input rows. `After`
counts the 1,463 suspect cells remaining in retained rows; 8 were removed with
the four discarded rows. The remaining cells are set to NaN for later
train-only imputation, not imputed yet.

## Extra Notes

- No exact duplicate rows, blank input cells, duplicate IDs, or invalid
  category codes were found.
- Four rows had suspect values in at least two predictor groups and were
  removed. Their observed `cardio` positive rate was 50%, compared with 49.97%
  overall. The removal is only 4 of 70,000 rows; this small-group comparison
  is not a formal bias test.
- Before removing multi-issue records, checks flagged 1,322 rows with blood
  pressure issues, 29 with suspect height, and 2 with suspect weight. After
  removal, 1,318 retained rows have suspect blood-pressure values set aside,
  along with 26 height values and 1 weight value. These counts can overlap.
  Suspect readings were set aside rather than guessed or used to discard
  otherwise usable records.
- Statistical outliers are not separately detected. Values within the selected
  plausibility checks are retained, even if they are unusual in the dataset.
- Formatting checks cover header normalization and leading/trailing whitespace
  in text cells. They do not attempt to standardize all possible numeric or
  categorical representations.

## How to run

1. Open a terminal at the project root.
2. Run the script with the member name and input CSV path:

   ```bash
   python3 <path-to-script>.py --member <member-name> --input <path-to-input-csv>
   ```

3. Find the cleaned CSV at `data/processed/<member-name>/cleaned_dataset.csv`.
   Running the command again with the same member name replaces that output.
