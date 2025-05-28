import numpy as np
import pandas as pd
import statsmodels
from itertools import combinations

import statsmodels.stats
import statsmodels.stats.contingency_tables
import statsmodels.stats.multitest
import stikpetP


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

def hypothesis_test(df: pd.DataFrame, variable: str) -> {}:
    # remember the second index is NOT inclusive, unlike .loc
    if variable == "principles":
        df = df[["Human autonomy", "Patient privacy", "Fairness", "Prevention of harm", "Explicability"]]
    elif variable == "pipeline":
        df = df[["Conception", "Calibration", "Development", "Implementation, Evaluation, and Oversight"]]
   
    # get overall cochran's q
    cochran_calc = statsmodels.stats.contingency_tables.cochrans_q(df)

    # get combinations of columns
    cc = list(combinations(df.columns,2))
    p_vals = {}
    statistics = {}
    degrees = {}
    comparisons = []

    # loop through combinations, compare them with Cochran's Q, and save them in p_vals dictionary
    for i in cc:
        frame1 = df.loc[:, [i[0]]]
        frame2 = df.loc[:, [i[1]]] 
        comparison_name = str(frame1.columns + " VS " + frame2.columns)
        comparisons.append(comparison_name)
        frames = frame1.join(frame2)
        cochran_calc_pair = statsmodels.stats.contingency_tables.cochrans_q(frames)
        # we get p-values, test statistics, and degrees of freedom according to the returned properties in https://www.statsmodels.org/stable/_modules/statsmodels/stats/contingency_tables.html#cochrans_q
        p_vals.update({comparison_name : cochran_calc_pair.pvalue})
        statistics.update({comparison_name : cochran_calc_pair.statistic})
        degrees.update({comparison_name : cochran_calc_pair.df})
    
    bonferroni_holm = statsmodels.stats.multitest.multipletests(list(p_vals.values()), method="holm")

    bonferroni_holm_dict = {key: value for key, value in zip(comparisons, list(bonferroni_holm[1]))}

    print(bonferroni_holm_dict)

    calc_dict = {
                        "Variable": variable, 
                        "Cochran's Q statistic" : cochran_calc.statistic,
                        "P-value" : cochran_calc.pvalue,
                        "df" : cochran_calc.df,
                        "Pairwise tests WITHOUT Holm-Bonferroni (p-values, statistics, df)" : [p_vals, statistics, degrees],
                        "Pairwise tests with Holm-Bonferroni (p-values)" : bonferroni_holm_dict,
                       }
    # return dict of chi_square values
    return calc_dict

def effect_size(df: pd.DataFrame, variable: str) -> {}:
    # remember the second index is NOT inclusive, unlike .loc
    if variable == "principles":
        df = df[["Human autonomy", "Patient privacy", "Fairness", "Prevention of harm", "Explicability"]]
    elif variable == "pipeline":
        df = df[["Conception", "Calibration", "Development", "Implementation, Evaluation, and Oversight"]]

    # set method to use for effect sizes
    method = "Berry-Johnston-Mielke R"

    # use the melt() method to create one table with variables and values - so 210 rows * the number of columns
    box = df.melt()
    crosstab = pd.crosstab(box.value, box.variable)
    print(crosstab)
    size = stikpetP.es_jbm_r(df)
    #sizes.append({comparison_name : size})

    #sizes_dict = {key: value for key, value in zip(comparisons, sizes)}
    final_dict = {"Method": method, "Variable": variable, "Effect size": size}

    return final_dict
