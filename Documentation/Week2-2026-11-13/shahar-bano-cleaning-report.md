# Kaggke CVD Data Cleaning Report
## Dataset information
**Name:** Kaggle Cardiovascular Disease dataset

**Number of rows:** 70,000

**Number of columns:** 13
## Data Quality Issues Found
**Missing values:** 0

**Duplicate rows:** 0

**Invalid records:** 0

**Outliers:** 0
## Cleaning Methods Used
Age was stored in days in the raw data, so each value was converted to years by dividing by 365.25 and rounding to one decimal place, and non-positive or non-numeric entries were set to blank. Height, weight, ap_hi, and ap_lo were parsed as numbers, and any non-numeric value was replaced with a blank field. Categorical columns (gender, cholesterol, gluc, smoke, alco, active, and the cardio target) were validated against their documented allowed codes, and any value outside that set was blanked. Outlier ranges are assumptions, not dataset-defined rules. Numeric values outside plausible physiological ranges were flagged as outliers and set to blank, using the ranges age 1–120 years, height 50–250 cm and weight 10–400 kg. Missing cells were written as empty fields in the output CSV, and the number of outliers flagged per column was recorded in the summary JSON. Duplicate rows were removed. Overall, the dataset was already clean; no missing values or duplicate rows were present in the raw file, and cleaning mainly normalized formats and guarded against implausible values.

## Before and After Summary
| Metric | Before | After |
|--------|--------|-------|
| Rows | 0 | 0 |
| Missing Values | 0 | 0 |
| Duplicates | 0 | 0 |