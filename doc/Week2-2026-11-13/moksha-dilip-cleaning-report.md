# Cleveland Heart Disease Data Cleaning Report

## Dataset information

I cleaned the UCI Cleveland Heart Disease dataset. The raw file
`processed.cleveland.data` contains 303 rows and 14 columns, including
the target column `num`.

## Data quality and cleaning methods

- I supplied column names because the raw file had no header.
- I trimmed whitespace and replaced six `?` markers with blank cells.
  I kept all records and left the missing values blank.
- I checked for exact duplicate rows and found zero.
- I checked that nonblank values could be read as finite numbers and
  that nonblank `num` values used codes from 0 through 4.

## Before and after

| Metric | Before | After |
| --- | ---: | ---: |
| Rows | 303 | 303 |
| Columns | 14 | 14 |
| Missing values | 6 | 6 |
| Exact duplicate rows | 0 | 0 |

## Potential outliers

I used the 1.5 × IQR rule to flag unusually low or high measurements.
I kept all flagged values for review. The counts are per column, so a
row can be counted in more than one column.

| Column | Flagged values |
| --- | ---: |
| `age` | 0 |
| `trestbps` | 9 |
| `chol` | 5 |
| `thalach` | 1 |
| `oldpeak` | 5 |

## How to reproduce

Put `processed.cleveland.data` in `data/raw/moksha-dilip/`. From the
repository root, run the following command.

    python3 src/data_cleaning/moksha-dilip-clean.py --member moksha-dilip --input processed.cleveland.data

The script writes `processed.cleveland_cleaned.csv` and
`processed.cleveland_summary.json` to `data/processed/moksha-dilip/`.