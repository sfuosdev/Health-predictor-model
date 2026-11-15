# Week 2 Dataset Acquisition and Evaluation

## Dataset 1 — Heart Disease (Cleveland subset)

- **Source** — UCI Machine Learning Repository
- **Records** — 303
- **Features** — 13
- **Prediction target** — `num`. For a yes/no model, `0` means heart disease is absent and `1–4` mean it is present.
- [UCI Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)

## Dataset 2 — Heart Failure Clinical Records

- **Source** — UCI Machine Learning Repository
- **Records** — 299
- **Features** — 12 columns excluding the target, including follow-up time
- **Prediction target** — `DEATH_EVENT`, whether a patient with heart failure died during follow-up.
- [UCI Heart Failure Clinical Records dataset](https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records)

## Dataset 3 — NHANES 2017–2018 Medical Conditions Questionnaire

- **Source** — CDC / National Center for Health Statistics
- **Raw file** — `MCQ_J.xpt`, the original SAS transport file
- **Records** — 8,897
- **Features** — 74 candidate questionnaire columns after excluding the participant ID and target. Some columns may be unsuitable as model inputs.
- **Prediction target** — `MCQ160C`, whether the participant reported being told by a health professional that they had coronary heart disease.
- **Target counts** — 265 yes, 5,288 no, 16 don't know, and 3,328 blank.
- [CDC dataset documentation](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/MCQ_J.htm)
- [CDC reuse guidance](https://www.cdc.gov/other/agencymaterials.html)

## Comparison

| Dataset | Advantage | Limitation or data quality concern |
| --- | --- | --- |
| UCI Cleveland | The clinical target can be grouped into yes/no heart disease. | It has 303 records and six missing values marked `?`. |
| UCI Heart Failure Clinical Records | The clinical measurements are documented, and the file has no blank cells. | It predicts death during follow-up in patients who already have heart failure. Follow-up duration would be unavailable at the first visit. |
| CDC NHANES | It has the largest sample and a documented coronary heart disease question. | Diagnosis history is self-reported. Only about 4.8% of definitive answers are positive, and many records have no usable target label. |

## Recommendation

I recommend UCI Cleveland for an initial model that classifies existing heart disease. The clinical target matches that goal, and the two classes are reasonably balanced after grouping the target into yes and no. The dataset is small, and the six missing values need handling before training.