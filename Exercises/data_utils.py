import matplotlib.pyplot as plt
import seaborn as sns 

def plot_missing_value(df):
    missing_counts = df.isnull().sum()
    missing_counts = missing_counts[missing_counts > 0]
    
    if missing_counts.empty:
        print("No missing values in the dataset")
        return

    plt.Figure(figsize=(10, 6))
    sns.barplot(x=missing_counts.index, y=missing_counts.values)
    plt.title("Missing values per column")
    plt.ylabel("Number of missing value")
    plt.xlabel("Columns")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()