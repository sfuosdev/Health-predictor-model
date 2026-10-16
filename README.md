<div align="center">

<img src="static/health_predictor_logo.png" alt="Cardiovascular Health Predictor Logo" width="180" />

# Cardiovascular Health Predictor

**An open-source machine learning project for exploring cardiovascular health data, developing predictive models, and evaluating statistical learning techniques.**

Developed and maintained by the **SFU Open Source Development Club (OS DEV)**.

</div>

---

## About the Project

Cardiovascular Health Predictor is an open-source machine learning project focused on exploring cardiovascular health datasets and developing statistical models to investigate patterns associated with cardiovascular disease.

The project aims to provide students with hands-on experience in the complete machine learning development lifecycle, from dataset selection and preprocessing to model training, evaluation, comparison, and interpretation.

Using Python and widely adopted machine learning libraries, contributors will work collaboratively to develop reproducible experiments, evaluate multiple classification algorithms, and communicate their findings through visualizations and technical documentation.

This project is part of the **SFU OS DEV Fall 2026 Open Source Project Initiative**, providing students with practical experience in machine learning, data science, statistics, and collaborative software development.

**Project Status:** Early Development — Dataset Selection & Research

> **Disclaimer:** This project is intended for educational and research purposes only. Its models are not validated medical devices and must not be used to diagnose cardiovascular conditions, make clinical decisions, or provide personalized medical advice.

## Project Objectives

The primary objectives of this project are to:

- Select and investigate an appropriate cardiovascular health dataset.
- Explore relationships between dataset features and cardiovascular outcomes.
- Perform data cleaning, preprocessing, and exploratory data analysis.
- Develop and train machine learning classification models.
- Compare different algorithms using appropriate evaluation metrics.
- Interpret model behavior and feature importance.
- Document experimental results, limitations, and potential improvements.
- Build a reproducible, collaborative machine learning workflow.

The specific prediction target and final research scope will be determined after the project team selects and evaluates a dataset.

## Key Features

The following capabilities are planned for development.

| Feature | Description | Status |
|---|---|---|
| Dataset Exploration | Analyze distributions, missing values, correlations, and feature characteristics | Planned |
| Data Preprocessing | Clean, encode, scale, and prepare data for machine learning | Planned |
| Predictive Modeling | Train classification models using scikit-learn | Planned |
| Model Comparison | Compare different algorithms and configurations | Planned |
| Model Evaluation | Evaluate accuracy, precision, recall, F1-score, and other relevant metrics | Planned |
| Feature Importance | Investigate which variables influence model predictions | Planned |
| Data Visualization | Present patterns and experimental results through graphs | Planned |
| Experiment Documentation | Record configurations, evaluation methods, and findings | Planned |

Additional features may be introduced based on the selected dataset, available resources, and project goals.

## Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | scikit-learn |
| Data Processing | pandas, NumPy |
| Development & Exploration | Jupyter Notebook |
| Data Visualization | Matplotlib, Seaborn |
| Model Evaluation | scikit-learn metrics |
| Testing | pytest (Planned) |
| Environment | Python Virtual Environment |
| Optional Containerization | Docker |
| CI/CD | GitHub Actions (Planned) |
| Version Control | Git, GitHub |

The final toolset may evolve as development progresses.

A web frontend, REST API, or cloud deployment is not required for the initial project scope. The focus is on developing and evaluating a reproducible machine learning pipeline.

## Machine Learning Pipeline

The project follows a structured machine learning workflow.

```text
                  Dataset Selection
                         |
                         v
                 Data Understanding
                         |
                         v
              Exploratory Data Analysis
                         |
                         v
                  Data Preprocessing
                         |
                         v
              Train / Validation / Test
                         |
                         v
                  Model Training
                         |
                         v
                Model Evaluation
                         |
                         v
                 Model Comparison
                         |
                         v
              Feature Interpretation
                         |
                         v
             Results & Documentation
```

### 1. Dataset Selection

The project begins by selecting a suitable, legally reusable cardiovascular health dataset.

The team should consider:

- Dataset origin and documentation
- Prediction target and available features
- Number of samples and class distribution
- Missing or inconsistent values
- Data quality and potential biases
- Privacy and licensing requirements
- Suitability for classification experiments

The dataset must be reviewed and approved by the Project Lead before being integrated into the repository.

### 2. Exploratory Data Analysis

Contributors will investigate the selected dataset using pandas, NumPy, and visualization tools.

Potential activities include:

- Inspecting dataset dimensions and feature types
- Identifying missing values
- Analyzing class distributions
- Visualizing numerical and categorical features
- Exploring correlations and relationships
- Identifying potential outliers
- Investigating possible class imbalance

The results should be documented in Jupyter Notebooks and summarized in project documentation.

### 3. Data Preprocessing

A preprocessing pipeline will be developed to prepare the dataset for machine learning.

Potential steps include:

- Handling missing values
- Removing invalid or duplicate records where appropriate
- Encoding categorical variables
- Scaling numerical features
- Creating reproducible training and testing partitions
- Applying class imbalance techniques when justified

Preprocessing transformations must be fitted using training data only to prevent data leakage into validation and test results.

### 4. Model Training

The team will train and evaluate a selection of machine learning algorithms.

Candidate models may include:

| Model | Purpose |
|---|---|
| Logistic Regression | Establish an interpretable classification baseline |
| Decision Tree | Explore rule-based decision boundaries |
| Random Forest | Evaluate ensemble-based classification |
| Support Vector Machine | Explore margin-based classification |
| Gradient Boosting | Investigate boosted ensemble performance |

The final selection will depend on dataset characteristics and project constraints.

### 5. Model Evaluation

Model performance will be assessed using appropriate classification metrics.

| Metric | Description |
|---|---|
| Accuracy | Proportion of correct predictions |
| Precision | Proportion of predicted positives that are actually positive |
| Recall | Proportion of actual positives correctly identified |
| F1-score | Harmonic mean of precision and recall |
| ROC-AUC | Ability to rank positive examples above negative examples |
| Confusion Matrix | Breakdown of classification outcomes |

Where applicable, the project may also investigate calibration, uncertainty, confidence intervals, and subgroup performance.

**Important:** Accuracy alone is not sufficient to judge model quality, particularly when the dataset contains imbalanced classes.

### 6. Feature Importance & Interpretation

The team will investigate how different input variables influence model behavior.

Potential techniques include:

- Logistic regression coefficient analysis
- Tree-based feature importance
- Permutation importance
- Partial dependence analysis
- Other appropriate interpretation techniques

Feature importance indicates relationships within the fitted model. It does not, by itself, establish causal relationships or clinical significance.

## Repository Structure

The planned repository structure is:

```text
cardiovascular-health-predictor/
├── assets/
│   └── cardiovascular-health-predictor-logo.png
│
├── data/
│   └── README.md
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── visualization.py
│
├── tests/
│   ├── test_preprocessing.py
│   └── test_evaluation.py
│
├── reports/
│   ├── figures/
│   └── results/
│
├── docs/
│   ├── dataset.md
│   ├── methodology.md
│   └── experiments.md
│
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
│
├── .gitignore
├── requirements.txt
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

This is the intended structure and may change during development. Planned files should not be treated as implemented functionality until they are added and tested.

Large datasets, sensitive records, generated model checkpoints, and temporary files should not be committed directly to the repository without review.

## Getting Started

We welcome students from Computing Science, Engineering Science, Statistics, Mathematics, Physics, and other disciplines interested in machine learning and data analysis.

### Prerequisites

The initial development environment requires:

- Python 3
- Git
- pip
- Jupyter Notebook or JupyterLab
- Visual Studio Code or another preferred IDE

### 1. Fork the Repository

Visit the official SFU OS DEV GitHub repository:

https://github.com/sfuosdev/cardiovascular-health-predictor

Click **Fork** to create a copy under your personal GitHub account.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/cardiovascular-health-predictor.git
cd cardiovascular-health-predictor
```

Replace `YOUR_USERNAME` with your GitHub username.

### 3. Configure Upstream

Connect your local repository to the official OS DEV repository.

```bash
git remote add upstream https://github.com/sfuosdev/cardiovascular-health-predictor.git
```

Verify the remotes:

```bash
git remote -v
```

### 4. Create a Python Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

Once the Project Lead has finalized the initial requirements, install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

The planned dependencies include:

```text
numpy
pandas
scikit-learn
matplotlib
seaborn
jupyterlab
pytest
```

The Project Lead will maintain version constraints in `requirements.txt`.

### 6. Launch JupyterLab

After installing the required packages:

```bash
jupyter lab
```

Open the available notebooks in the `notebooks/` directory.

**Note:** The repository is in its initial development stage. Notebooks, Python scripts, and automated tests will become available as contributors implement the project.

## Dataset Management

The project will use a publicly available dataset with appropriate usage rights.

Dataset selection and documentation should be completed before model development begins.

### Dataset Requirements

The selected dataset should:

- Have a clearly defined target variable.
- Include sufficient documentation of its features.
- Have a license or usage terms compatible with the intended research.
- Avoid exposing personally identifiable or confidential health information.
- Be suitable for reproducible analysis.
- Support meaningful model training and evaluation.

### Dataset Documentation

Once selected, `docs/dataset.md` should document:

- Dataset name and original source
- Dataset license and usage conditions
- Prediction target
- Feature descriptions
- Sample count and class distribution
- Missing values and known limitations
- Data acquisition instructions
- Citation and attribution requirements

Contributors should not upload restricted medical data or identifiable patient records.

If external data cannot be redistributed, the repository should provide acquisition instructions rather than including the dataset.

## Reproducibility & Experiment Tracking

Reproducibility is an important objective of this project.

Contributors should document:

- Dataset version
- Preprocessing configuration
- Training and validation methodology
- Random seeds
- Model hyperparameters
- Evaluation metrics
- Experimental results
- Relevant software dependency versions

Model comparisons should use consistent evaluation protocols.

The final test set should be reserved for evaluation rather than repeatedly used to select models or tune hyperparameters.

Experiment results should be documented in `docs/experiments.md` or a similarly maintained record.

## Development Roadmap

### Phase 1 — Project Initialization

- [ ] Initialize Python project structure
- [ ] Configure virtual environment and dependencies
- [ ] Establish GitHub contribution guidelines
- [ ] Configure basic CI and automated testing
- [ ] Research candidate cardiovascular datasets
- [ ] Select and document the dataset

### Phase 2 — Data Exploration

- [ ] Load and inspect the dataset
- [ ] Analyze feature distributions
- [ ] Investigate missing and invalid values
- [ ] Examine class distribution
- [ ] Generate exploratory visualizations
- [ ] Document dataset limitations

### Phase 3 — Data Preprocessing

- [ ] Establish data splitting strategy
- [ ] Implement missing value handling
- [ ] Encode categorical variables
- [ ] Apply appropriate feature scaling
- [ ] Implement preprocessing pipelines
- [ ] Add tests to prevent data leakage

### Phase 4 — Model Development

- [ ] Implement an initial baseline classifier
- [ ] Train Logistic Regression
- [ ] Train Decision Tree
- [ ] Train Random Forest
- [ ] Investigate additional model architectures
- [ ] Perform justified hyperparameter tuning

### Phase 5 — Model Evaluation

- [ ] Evaluate classification performance
- [ ] Generate confusion matrices
- [ ] Compare precision, recall, and F1-score
- [ ] Evaluate ROC-AUC where applicable
- [ ] Investigate feature importance
- [ ] Discuss model limitations and potential biases

### Phase 6 — Results & Presentation

- [ ] Consolidate experimental results
- [ ] Create final visualizations
- [ ] Document model comparisons
- [ ] Prepare methodology and findings
- [ ] Complete technical documentation
- [ ] Present project outcomes to SFU OS DEV

The Project Lead will coordinate the development schedule and milestone priorities with the project team.

## Contributing

Contributions are welcome from students and developers interested in machine learning, statistics, data processing, software engineering, and technical documentation.

### Contribution Workflow

1. **Find an Issue** — Review available GitHub Issues.
2. **Fork the Repository** — Create your personal copy.
3. **Clone Your Fork** — Set up your local development environment.
4. **Create a Feature Branch** — Keep each task isolated.
5. **Develop & Test** — Implement and validate your changes.
6. **Push Changes** — Push commits to your fork.
7. **Submit a Pull Request** — Propose changes to the official repository.
8. **Review & Merge** — Maintainers review and merge approved contributions.

### Branch Naming Conventions

```text
feature/data-preprocessing
feature/logistic-regression
feature/model-comparison
feature/feature-importance

fix/missing-values
fix/data-leakage

docs/dataset-documentation
test/preprocessing-pipeline
```

### Example Git Workflow

Synchronize your local branch:

```bash
git switch main
git fetch upstream
git merge upstream/main
```

Create a feature branch:

```bash
git switch -c feature/model-evaluation
```

Commit your changes:

```bash
git add .
git commit -m "feat: implement model evaluation metrics"
```

Push your branch:

```bash
git push -u origin feature/model-evaluation
```

Open a Pull Request targeting the official OS DEV repository's `main` branch.

For detailed contribution guidelines, refer to [CONTRIBUTING.md](CONTRIBUTING.md) once available.

## Project Management

The project will use GitHub Issues, GitHub Projects, and Pull Requests to organize development.

### GitHub Issues

Issues will be used to track:

- Dataset research
- Data preprocessing tasks
- Exploratory analysis
- Model development
- Evaluation experiments
- Testing and debugging
- Visualization
- Documentation

### GitHub Projects

| Stage | Description |
|---|---|
| Backlog | Proposed research and development tasks |
| To Do | Tasks approved for development |
| In Progress | Active implementation or experimentation |
| In Review | Changes awaiting review |
| Done | Completed and merged work |

### Pull Request Guidelines

Each Pull Request should include:

- A description of changes
- A linked Issue when applicable
- Testing or evaluation performed
- Relevant charts or results when applicable
- Changes to documentation
- Notes about reproducibility and limitations

Contributors should avoid including unnecessarily large notebook outputs, generated model artifacts, or private datasets in their commits.

## Team Collaboration

The project will be developed collaboratively under the guidance of a Project Lead.

### Project Lead Responsibilities

- Coordinate dataset selection and research direction.
- Organize project milestones and sprints.
- Assign GitHub Issues to contributors.
- Maintain consistent preprocessing and evaluation standards.
- Review Pull Requests.
- Ensure experiments are reproducible.
- Organize team meetings and progress updates.
- Represent the project during OS DEV executive checkup meetings.

### Project Member Responsibilities

- Attend scheduled team meetings.
- Select or accept assigned GitHub Issues.
- Develop and test assigned tasks.
- Document experimental methods and results.
- Communicate blockers and progress.
- Submit Pull Requests for review.
- Follow the project's contribution guidelines.

Project members from different academic backgrounds are encouraged to contribute according to their interests and experience.

## Research Ethics & Responsible Machine Learning

This project involves health-related data and predictions, which require particular care.

All contributors should follow these principles:

- Use appropriately licensed datasets.
- Respect privacy, confidentiality, and data protection requirements.
- Do not upload identifiable patient data.
- Evaluate potential dataset biases and limitations.
- Avoid presenting correlation or feature importance as evidence of causation.
- Document model uncertainty and limitations.
- Avoid unsupported claims about real-world medical effectiveness.
- Do not deploy the models as clinical diagnostic or treatment systems.

**All predictions, analyses, and visualizations are for educational and research purposes only.**

## Team & Maintainers

**Organization:** SFU Open Source Development Club (OS DEV)

**Academic Term:** Fall 2026

**Project Lead:** To be assigned

**Project Contributors:** To be announced

This project is maintained collaboratively by students interested in machine learning, data science, statistics, and open-source development.

## Learning Objectives

Through this project, contributors will gain hands-on experience in:

- Python programming for data science
- Exploratory data analysis
- Dataset cleaning and preprocessing
- Supervised machine learning
- Classification algorithms
- Model evaluation and comparison
- Statistical reasoning
- Feature importance and interpretation
- Reproducible experiments
- Technical documentation
- Git and GitHub collaboration
- Pull Requests and code reviews
- Research presentation and teamwork

Our goal is to provide an accessible learning environment where students can explore machine learning through collaborative research and software development.

## License

This project is intended to be released under the MIT License, subject to confirmation of contributor rights and third-party licensing requirements.

Once finalized, the full license terms will be available in the repository's `LICENSE` file.

Any selected dataset remains subject to its own licensing, attribution, and redistribution requirements.

## Connect With SFU OS DEV

- **GitHub Organization:** https://github.com/sfuosdev
- **Instagram:** https://www.instagram.com/sfu_osdev/
- **SFSS Club Page:** https://go.sfss.ca/clubs/867/info

---

**Built by students, driven by research.**

*SFU Open Source Development Club — Design. Develop. Deploy.*
