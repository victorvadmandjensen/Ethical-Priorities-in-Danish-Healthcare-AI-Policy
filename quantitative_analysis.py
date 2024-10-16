import numpy as np
import pandas as pd

from load_data import load_data, transform_data
from statistic_calcs import descriptive_stats
from visualization import create_bar_chart

# force pandas to show all columns
pd.set_option('display.max_columns', None)


file_path = "Test_data.xlsx"
sheet = "Data charting, 25 sep TEST"

document_chars = ["Language", "Publication year", "Publishing institution", "Document type"]
principles = ["Human autonomy", "Patient privacy", "Fairness", "Prevention of harm", "Explicability"]
pipeline = ["Conception", "Development", "Calibration", "Implementation, Evaluation, and Oversight"]



dataframe = load_data(file_path, sheet)

dataframe = transform_data(dataframe, principles, pipeline)
#print(dataframe)

doc_dataframe, ethics_dataframe = descriptive_stats(dataframe, [document_chars, principles, pipeline])

create_bar_chart(ethics_dataframe, "principles")