import numpy as np
import pandas as pd
import statsmodels as sm

def descriptive_stats(df: pd.DataFrame, columns = []) -> pd.DataFrame:
    ethics_df = {}
    doc_df = {}

    # flatten list of columns
    columns = [col for sublist in columns for col in sublist]
    selected_columns = df[columns]
    
    for column in selected_columns:
        if pd.api.types.is_numeric_dtype(df[column]):
        # get sums, reset_index for readability, and rename
            ethics_df[column] = df[column].sum()
        elif pd.api.types.is_object_dtype(df[column]):
            doc_df[column] = df[column].value_counts()
    ethics_df = pd.DataFrame(ethics_df.items(), columns=["RQ1 variable", "Count of appearances"])
    doc_df = pd.DataFrame(doc_df.items(), columns=["Document characteristic", "count of appearances"])

    return doc_df, ethics_df

def chi_square() -> pd.DataFrame:
    print("lol")
