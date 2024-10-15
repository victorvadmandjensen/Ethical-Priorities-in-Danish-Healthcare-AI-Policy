import numpy as np
import pandas as pd

# force pandas to show all columns
pd.set_option('display.max_columns', None)


def load_data(path: str, sheet: str) -> pd.DataFrame:
    # read xlsx file and drop columns after RQ1
    file = pd.read_excel(path, sheet_name=sheet, header=1)
    file.drop(file.columns[16:], axis=1, inplace=True)

    return file

def transform_data(df: pd.DataFrame, principles: [], pipeline: []) -> pd.DataFrame:
    # loop through lists, put 0 in empty columns from list and create list from new_name with binarized values
    item_list = [principles, pipeline]
    for i in item_list:
        for item in i:
            df[item].fillna(0, inplace=True)
            new_name = str(item) + ", binary"
            # create new_name as column and insert 0 if value is 0 else 1
            df[new_name] = np.where(df[item] == 0, 0, 1)
            df.drop(columns=[item], inplace=True)

    return df


file_path = "Test_data.xlsx"
sheet = "Data charting, 25 sep TEST"

principles = ["Human autonomy", "Patient privacy", "Fairness", "Prevention of harm", "Explicability"]
pipeline = ["Conception (Auditability, Transparency Standards, and Conflicts of Interest)",
                                         "Development (Perpetuation of Bias within Training Data, Risk of Harm due to Group Membership, and Obtaining Training Data)",
                                         "Calibration (Accuracy, Trading Off Test Characteristics, and Calibrated Risk of Harm)",
                                         "Implementation, Evaluation, and Oversight (Adverse Events, Ongoing Assessment of Accuracy and Usage)"]



dataframe = load_data(file_path, sheet)

transform_data(dataframe, principles, pipeline)
