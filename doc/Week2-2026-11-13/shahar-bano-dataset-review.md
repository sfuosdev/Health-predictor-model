# Cardiovascular Disease Dataset Review

## Dataset 1
**Name:** Cardiovascular Disease dataset

**Source:** Kaggle.com

**# of Records:** 70,000

**# of Features:** 12

**Prediction Target:** Cardiovascular disease (0 = no CVD, 1 = has CVD) 
**Link:** https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset/data

## Dataset 2
**Name:** Heart Disease

**Source:** UC Irvine Machine Learning Repository

**# of Records:** 303

**# of Features:** 13

**Prediction Target:** Degree of CVD (0 = healthy, 1-4 = varying degrees of CVD)

**Link:** https://archive.ics.uci.edu/dataset/45/heart+disease

---

## Comparison

### Advantages
**Dataset 1:**
- Much more extensive, which is better for training ML models
- No missing values
- Already cleaned and formatted as a standard CSV
- Has a header
- Values are easy to interpret


**Dataset 2:**
- Contains more clinical features (like fasting blood sugar, chest pain type, exercise induced angina) that offer more medical context
- 


### Disadvantages + Concerns

**Dataset 1:**
- Lacks much clinical context
- Partially synthetic/anonymized, meaning real-world edge cases might be missing

**Dataset 2:**
- Couple missing values, denoted by '?"
- Smaller dataset
- Collected in 1989 (outdated data)
- Values are harder to interpret without .names file
- No header



## Recommendation
I recommend the Kaggle dataset because of its sheer size and cleanliness. With 70,000 records, we can build complex, robust machine learning models without the risk of severe overfitting (which is a major concern with Dataset 2's 303 records). Furthermore, because Dataset 1 has no missing values and is already formatted with a header, it allows us to spend our project time on feature engineering, model selection, and evaluation rather than extensive data cleaning. 