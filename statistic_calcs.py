import numpy as np
import pandas as pd
import samplics.datasets
import statsmodels as sm
import scipy.stats as stats
import samplics

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
    # create dataframe for ethics and for each of the categorical variables to concat these
    ethics_df = pd.DataFrame(ethics_df.items(), columns=["RQ1 variable", "Count of appearances"])
    lang_df = pd.DataFrame(doc_df["Language"].items(), columns=["Document characteristic", "count of appearances"])
    year_df = pd.DataFrame(doc_df["Publication year"].items(), columns=["Document characteristic", "count of appearances"])
    inst_df = pd.DataFrame(doc_df["Publishing institution"].items(), columns=["Document characteristic", "count of appearances"])
    type_df = pd.DataFrame(doc_df["Document type"].items(), columns=["Document characteristic", "count of appearances"])

    doc_df = pd.concat([lang_df, year_df, inst_df, type_df], axis=0)
    #print(ethics_df)

    return ethics_df, doc_df

def chi_square(df: pd.DataFrame, variable: str) -> {}:
    # remember the second index is NOT inclusive, unlike .loc
    if variable == "principles":
        #df = df.iloc[0:5]
        df = df[["Human autonomy", "Patient privacy", "Fairness", "Prevention of harm", "Explicability"]]
    elif variable == "pipeline":
        df = df[["Conception" "Calibration", "Development", "Implementation, Evaluation, and Oversight"]]
   
    #print(df["Explicability"])
    new_list = [1 if i % 2 == 0 else 0 for i in range(0, 210)]
    equal_dist = pd.DataFrame(np.array(new_list))
    equal_dist.columns = ["Expected"]
    equal_dist["Explicability"] = df["Explicability"]
    #print(equal_dist.columns)

    new_df = df#.transpose()
    print(new_df)

    print("Samplics analysis starts... \n")

    table = samplics.Tabulation(samplics.PopParam.count)
    #table.tabulate(samplics.datasets.load_birth()["data"].astype({"birthcat":str})["birthcat"], remove_nan=True)
    table.tabulate(vars = new_df, remove_nan=False)
    print(table)
    #print(table.stats)

    print("Samplics analysis ends... \n")


    # get expected values as sum of appearances over number of categories
    exp = df["Count of appearances"].sum() / len(df.index)

    chi_square_calc = stats.chisquare(f_obs=df["Count of appearances"], f_exp=exp)
    chi_square_dict = {
                        "Variable": variable, 
                        "Chi-square statistic" : chi_square_calc.statistic,
                        "P-value" : chi_square_calc.pvalue
                       }
    # return dict of chi_square values
    return chi_square_dict