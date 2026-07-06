import pandas as pd

def load_dataset():

    df = pd.read_csv("data/raw/creditcard.csv")

    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFraud Class Distribution:")
    print(df["Class"].value_counts())

    print("\nFraud Class Percentage:")
    print(df["Class"].value_counts(normalize=True) * 100)

    print("\nSummary Statistics:")
    print(df.describe())

    return df