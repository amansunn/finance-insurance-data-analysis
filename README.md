# Finance and Insurance Data Analysis Project

This project aims to perform data analysis in the finance and insurance sectors. It includes data processing, exploratory data analysis (EDA), and version control for datasets using DVC (Data Version Control).

## Project Structure

- **data/**: Contains raw and processed datasets.
  - **raw/**: Directory for raw datasets used for analysis.
  - **processed/**: Directory for processed datasets after cleaning and transformations.
  
- **dvc.yaml**: Configuration file for DVC, defining the data pipeline and processing stages.

- **.dvc/**: Contains DVC metadata and configuration files for tracking data versions.

- **.gitignore**: Specifies files and directories to be ignored by Git.

- **.github/workflows/**: Contains CI/CD configuration for GitHub Actions.
  - **ci-cd.yml**: Configuration for build and test workflows.

- **notebooks/**: Contains Jupyter notebooks for analysis.
  - **exploratory_data_analysis.ipynb**: Notebook for performing EDA, including visualizations and statistical analysis.

- **src/**: Contains source code for data analysis.
  - **eda.py**: Functions and classes for EDA, including methods for calculating loss ratios and generating plots.
  - **utils.py**: Utility functions for data processing and analysis.

- **requirements.txt**: Lists dependencies required for the project, including libraries for data analysis, visualization, and DVC.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd finance-insurance-data-analysis
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Initialize DVC:
   ```
   dvc init
   ```

4. Add your raw data to the `data/raw` directory and track it with DVC:
   ```
   dvc add data/raw/<your-dataset>
   ```

5. Run the DVC pipeline:
   ```
   dvc repro
   ```

## Task Workflow and Branching

### Git Branching and Commit Strategy
- Create a new branch for each major task (e.g., `task-1`, `task-2`).
- Commit work at least three times per day with descriptive messages (e.g., `Initial EDA summary`, `Added loss ratio plots`, `Refactored data quality checks`).
- Use Pull Requests (PRs) to merge feature branches into `main` after review.

### CI/CD with GitHub Actions
- Linting and notebook checks are run automatically on push and PRs to `main`.
- DVC steps are included in the workflow for data versioning.

## DVC Usage

1. **Install DVC** (if not already):
   ```cmd
   pip install dvc
   ```
2. **Initialize DVC** (already done):
   ```cmd
   dvc init
   ```
3. **Set up local remote storage** (already done):
   ```cmd
   dvc remote add -d localstorage dvc_storage
   ```
4. **Add your data** (already done for MachineLearningRating_v3.txt):
   ```cmd
   dvc add data/raw/MachineLearningRating_v3.txt
   ```
5. **Commit DVC files and push data to remote**:
   ```cmd
   git add data/raw/MachineLearningRating_v3.txt.dvc .gitignore
   git commit -m "Track data with DVC"
   dvc push
   ```

## Usage Guidelines

- Use the Jupyter notebook in `notebooks/exploratory_data_analysis.ipynb` for EDA.
- Utilize the functions in `src/eda.py` for specific analysis tasks.
- Use `src/utils.py` for data loading and cleaning tasks.

## EDA Steps
- Data summarization: descriptive statistics, dtype review, missing value checks.
- Univariate analysis: histograms/bar charts for key variables.
- Bivariate/multivariate analysis: scatter plots, correlation matrix, box plots for outlier detection.
- At least 3 creative and beautiful plots with clear insights.

## References
- [DVC Documentation](https://dvc.org/doc)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Documentation](https://seaborn.pydata.org/)

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.