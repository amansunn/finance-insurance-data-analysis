def load_data(file_path):
    import pandas as pd
    """Load data from a CSV file."""

    try:
        if file_path.endswith('.txt'):
            data = pd.read_table(file_path, sep='|')  # Specify pipe delimiter for .txt files
        else:
            data = pd.read_csv(file_path)
        print(f"Data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Clean the DataFrame by handling missing values and duplicates."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def generate_descriptive_statistics(df):
    """Generate descriptive statistics for the DataFrame."""
    return df.describe()

def save_data(df, file_path):
    """Save the DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)