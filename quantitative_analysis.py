import pandas as pd

from load_data import load_data, transform_data, save_data
from statistic_calcs import descriptive_stats, hypothesis_test, effect_size
from visualization import create_bar_chart, create_descriptive_charts
from datetime import datetime

import numpy as np

import config

# force pandas to show all columns
pd.set_option('display.max_columns', None)

file_path = config.file_path
sheet = config.sheet


document_chars = ["Language", "Publication year", "Publishing institution", "Document type"]
principles = ["Human autonomy", "Patient privacy", "Fairness", "Prevention of harm", "Explicability"]
pipeline = ["Conception", "Development", "Calibration", "Implementation, Evaluation, and Oversight"]



dataframe = load_data(file_path, sheet)

dataframe = transform_data(dataframe, principles, pipeline, document_chars)

ethics_df, doc_df = descriptive_stats(dataframe, [document_chars, principles, pipeline])

# use records for a more human-readable output
doc_df = doc_df.to_dict(orient="records")

result_list = [
    hypothesis_test(dataframe, "pipeline"),
    hypothesis_test(dataframe, "principles"),
    effect_size(dataframe, "pipeline"),
    effect_size(dataframe, "principles"),
    doc_df
]

save_data(str(datetime.today()), result_list)

color1 = "#005f2f"
color2 = "#00005f"
color3 = "#8BAD3F"
color4 = "#FABB00"

create_bar_chart(ethics_df, "pipeline", color2)
create_bar_chart(ethics_df, "principles", color1)

create_descriptive_charts(dataframe)