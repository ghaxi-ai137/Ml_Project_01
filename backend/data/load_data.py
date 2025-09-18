import pandas as pd
import seaborn as sns

#  write a function to load the data
def load_data():
    """Load the dataset and return a pandas DataFrame."""
    df = sns.load_dataset("tips")
    return df