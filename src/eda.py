def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def calculate_loss_ratio(data):
    data['loss_ratio'] = data['losses'] / data['premiums']
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
    if hue:
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