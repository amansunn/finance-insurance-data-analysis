def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def calculate_loss_ratio(data):
    data['loss_ratio'] = data['TotalClaims'] / data['TotalPremium']
    return data

def summarize_data(data):
    summary = {
        'mean_loss_ratio': data['loss_ratio'].mean(),
        'median_loss_ratio': data['loss_ratio'].median(),
        'std_loss_ratio': data['loss_ratio'].std(),
        'count': data['loss_ratio'].count()
    }
    return summary

def plot_loss_ratio(data):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(10, 6))
    sns.histplot(data['loss_ratio'], bins=30, kde=True)
    plt.title('Distribution of Loss Ratios')
    plt.xlabel('Loss Ratio')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

def review_data_types(data):
    """Review data types of each column."""
    return data.dtypes

def check_missing_values(data):
    """Check for missing values in each column."""
    return data.isnull().sum()

def descriptive_statistics(data, columns=None):
    """Get descriptive statistics for specified columns or all numerical columns."""
    if columns is None:
        columns = data.select_dtypes(include=['number']).columns
    return data[columns].describe()

def plot_histograms(data, columns):
    import matplotlib.pyplot as plt
    data[columns].hist(bins=30, figsize=(15, 8), layout=(1, len(columns)))
    plt.suptitle('Histograms of Numerical Columns')
    plt.show()

def plot_bar_chart(data, column):
    import matplotlib.pyplot as plt
    data[column].value_counts().plot(kind='bar', figsize=(8, 5))
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

def plot_scatter(data, x, y, hue=None):
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    if hue and hue in data.columns:
        sns.scatterplot(data=data, x=x, y=y, hue=hue)
    else:
        sns.scatterplot(data=data, x=x, y=y)
    plt.title(f'Scatter plot of {y} vs {x}')
    plt.show()

def plot_correlation_matrix(data, columns=None):
    import seaborn as sns
    import matplotlib.pyplot as plt
    if columns is None:
        columns = data.select_dtypes(include=['number']).columns
    corr = data[columns].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def plot_boxplot(data, column, by=None):
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    if by:
        sns.boxplot(x=by, y=column, data=data)
        plt.title(f'Boxplot of {column} by {by}')
    else:
        sns.boxplot(y=data[column])
        plt.title(f'Boxplot of {column}')
    plt.show()

# Example creative plot: Loss Ratio by Province and VehicleType

def plot_loss_ratio_by_group(data, group_col):
    import matplotlib.pyplot as plt
    import seaborn as sns
    group_loss = data.groupby(group_col)['loss_ratio'].mean().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=group_loss.index, y=group_loss.values)
    plt.title(f'Average Loss Ratio by {group_col}')
    plt.xlabel(group_col)
    plt.ylabel('Average Loss Ratio')
    plt.xticks(rotation=45)
    plt.show()

import numpy as np
from scipy import stats

def claim_frequency(data, group_col=None):
    if group_col:
        return data.groupby(group_col)['TotalClaims'].apply(lambda x: (x > 0).mean())
    return (data['TotalClaims'] > 0).mean()

def claim_severity(data, group_col=None):
    if group_col:
        return data[data['TotalClaims'] > 0].groupby(group_col)['TotalClaims'].mean()
    return data[data['TotalClaims'] > 0]['TotalClaims'].mean()

def margin(data, group_col=None):
    if group_col:
        return data.groupby(group_col).apply(lambda x: (x['TotalPremium'] - x['TotalClaims']).mean())
    return (data['TotalPremium'] - data['TotalClaims']).mean()

def t_test_groups(data, group_col, metric_col, group_a, group_b):
    group_a_data = data[data[group_col] == group_a][metric_col]
    group_b_data = data[data[group_col] == group_b][metric_col]
    t_stat, p_val = stats.ttest_ind(group_a_data, group_b_data, nan_policy='omit')
    return t_stat, p_val

def chi2_test_groups(data, group_col, outcome_col, group_a, group_b):
    contingency = np.array([
        [(data[(data[group_col]==group_a) & (data[outcome_col]>0)].shape[0]),
         (data[(data[group_col]==group_a) & (data[outcome_col]==0)].shape[0])],
        [(data[(data[group_col]==group_b) & (data[outcome_col]>0)].shape[0]),
         (data[(data[group_col]==group_b) & (data[outcome_col]==0)].shape[0])]
    ])
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    return chi2, p