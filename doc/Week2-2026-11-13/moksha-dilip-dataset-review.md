# Week 2 Dataset Acquisition and Evaluation

## Dataset 1 — Heart Disease (Cleveland subset)

- **Source:** UCI Machine Learning Repository
- **Records:** 303
- **Features:** 13 input columns
- **Prediction target:** `num`, which records heart disease status. For a yes/no model, `0` means absent and `1–4` mean present.
- **Link:** [UCI Heart Disease](https://archive.ics.uci.edu/dataset/45/heart+disease)

## Dataset 2 — Heart Failure Clinical Records

- **Source:** UCI Machine Learning Repository
- **Records:** 299
- **Features:** 12 input columns, including follow-up time
- **Prediction target:** `DEATH_EVENT`, whether a patient with heart failure died during follow-up.
- **Link:** [UCI Heart Failure Clinical Records](https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records)

## Dataset 3 — Heart Failure Prediction Dataset

- **Source:** Kaggle, uploaded by fedesoriano
- **Records:** 918
- **Features:** 11 input columns
- **Prediction target:** `HeartDisease`, where `1` means heart disease is present and `0` means it is absent.
- **Link:** [Kaggle Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

## Comparison

| Dataset | Advantage | Limitation or data quality concern |
| --- | --- | --- |
| Cleveland | UCI explains the variables, and the target can be grouped into yes/no heart disease. | It has only 303 records and contains missing values. |
| Heart Failure Clinical Records | UCI reports no missing values, and the clinical measurements are documented. | It predicts death among people who already have heart failure. Follow-up time would be unavailable for a prediction made at the first visit. |
| Kaggle | It has the most records of the three and a yes/no heart disease target. | Some cholesterol and resting blood pressure values are zero and need checking. It includes Cleveland records, so Cleveland should not serve as an independent test set for a model trained on it. |

## Recommendation

I recommend the Kaggle dataset for an initial model that classifies whether heart disease is already present. It has 918 records and a target that matches that question. Before training, I would check the zero cholesterol and resting blood pressure values and document how we handle them. I would also confirm the dataset's license before adding it to the public project repository.