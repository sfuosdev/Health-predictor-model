## Dataset 1
- **Name:** Cardiovascular Disease dataset (sulianova)
- **Source:** Kaggle
- **Number of Records:** 70,000 rows
- **Number of Features:** 13 columns
- **Prediction Target:** `cardio` (whether a patient has cardiovascular disease: 0 = No, 1 = Yes)
- **Link:** [Cardiovascular Disease Dataset – Kaggle](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)

## Dataset 2
- **Name:** Cardiovascular Disease dataset (colewelkins)
- **Source:** Kaggle
- **Number of Records:** 68,205 rows
- **Number of Features:** 17 columns
- **Prediction Target:** `cardio` (0 = No cardiovascular disease, 1 = Has cardiovascular disease)
- **Link:** [Cardiovascular Disease Dataset – Kaggle](https://www.kaggle.com/datasets/colewelkins/cardiovascular-disease)

## Dataset 3
- **Name:** Heart Disease dataset (UCI Machine Learning Repository)
- **Source:** UCI Machine Learning Repository
- **Number of Records:** 303 rows
- **Number of Features:** 13 columns
- **Prediction Target:** `num` (0 = No heart disease, 1–4 = Presence of heart disease)
- **Link:** [Heart Disease Dataset – UCI](https://archive.ics.uci.edu/dataset/45/heart+disease)

## Comparison

### Discuss:

- Advantages of each dataset
    - Dataset 1: 
        - Largest of the 3 datasets (at 70,000 rows)
        - Contains a wide range of physiological factors (fields)
        - Cardio target has clear yes or no
        - No missing reported values 
    - Dataset 2:
        - Similarly large dataset (68,205 rows)
        - Contains 17 fields
        - Contains additional derived features, such as BMI and blood pressure categories
    - Dataset 3:
        - Has a clearly defined prediction target `num`
        - `num` lists if they have multiple cardiovascular disease
        - Comes from an established machine learning repository and is used in academic research
        - Contains clinically relevant features, such as chest pain type, cholesterol, resting blood pressure, and maximum heart rate

- Disadvantages of each dataset
    - Dataset 1:
        - Does not include every possible factor that contributes to cardiovascular disease
        - May not represent all age groups and demographic populations equally
    - Dataset 2:
        - Contains outliers that may negatively affect model accuracy
        - Some features are derived from existing variables, meaning there may be redundant information
    - Dataset 3:
        - Contains only 303 records
        - Contains a target with five possible values (0–4), which may require additional preprocessing if our model only wants a yes or no prediction

- Data quality concerns
    - Dataset 1:
        - Duplicate records may cause the model to learn repeated patterns
        - Age is recorded in days rather than years, requiring conversion for easier interpretation
        - Potential demographic imbalances may affect how well the model performs on different populations
    - Dataset 2:
        - Contains approximately 6,494 identified outliers across several variables, including BMI, height, weight, and blood pressure 
        - Extreme values may distort statistical analysis and affect model training
        -Derived features, such as BMI and blood pressure categories, should be checked for consistency with their original measurements
        - The dataset should be checked for duplicate records and missing values before training
    - Dataset 3:
        - The dataset is relatively old, with data originating from the 1980s
        - The relatively small number of records may limit the model's ability to generalize
        - Missing values are present in attributes such as `ca` and `thal`
        - Not in `.csv` format

- Which dataset you recommend and why
    - Dataset 1 (sulianova)
    - Why: I recommend Dataset 1 (Sulianova – Kaggle) because it offers 70,000 records, relevant health features, and a straightforward binary prediction target (`cardio`). Its CSV format also makes it easy to work with Python libraries. Compared with the other datasets, it provides the best balance of data size, accessibility, and ease of implementation for our machine learning project.
