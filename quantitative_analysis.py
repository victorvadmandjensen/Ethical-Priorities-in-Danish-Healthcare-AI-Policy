import pandas as pd

from load_data import load_data, transform_data, save_data
from statistic_calcs import descriptive_stats, chi_square
from visualization import create_bar_chart
from datetime import datetime

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

result_list = [
    chi_square(ethics_df, "pipeline"),
    chi_square(ethics_df, "principles"),
    # use records for a more human-readable output
    doc_df.to_dict(orient="records")
]

save_data(str(datetime.today()), result_list)

create_bar_chart(ethics_df, "pipeline")
