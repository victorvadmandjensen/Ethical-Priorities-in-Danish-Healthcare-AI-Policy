import numpy as np
import pandas as pd
import json
from datetime import datetime

def load_data(path: str, sheet: str) -> pd.DataFrame:
    # read xlsx file and drop first column and columns after RQ1
    file = pd.read_excel(path, sheet_name=sheet, header=1)
    file.drop(file.columns[16:], axis=1, inplace=True)
    file.drop(file.columns[0], axis=1, inplace=True)
    # cast pub year column to object
    file["Publication year"] = file["Publication year"].astype(object)

    return file

def transform_data(df: pd.DataFrame, principles: [], pipeline: [], document_chars: []) -> pd.DataFrame:
    # rename pipeline columns with zipped dict from lists
    original_pipeline_cols = ["Conception (Auditability, Transparency Standards, and Conflicts of Interest)",
                                         "Development (Perpetuation of Bias within Training Data, Risk of Harm due to Group Membership, and Obtaining Training Data)",
                                         "Calibration (Accuracy, Trading Off Test Characteristics, and Calibrated Risk of Harm)",
                                         "Implementation, Evaluation, and Oversight (Adverse Events, Ongoing Assessment of Accuracy and Usage)"]
    new_pipeline_cols = pipeline
    pipeline_dict = dict(zip(original_pipeline_cols,new_pipeline_cols))

    df = df.rename(columns=pipeline_dict)

    # loop through lists, put 0 in empty columns from list and create list from new_name with binarized values
    item_list = [principles, pipeline]
    for i in item_list:
        for item in i:
            df[item].fillna(0, inplace=True)
            new_name = str(item) 
            # create new_name as column and insert 0 if value is 0 else 1
            df[new_name] = np.where(df[item] == 0, 0, 1)

    return df

def save_data(dt: datetime, dict_list: []):
    # create datetime dict and insert at beginning of dict_list
    dt_dict = {"Datetime": dt}
    dict_list.insert(0, dt_dict)

    with open("results.json", "w") as fp:
        json.dump(dict_list, fp, indent=4)