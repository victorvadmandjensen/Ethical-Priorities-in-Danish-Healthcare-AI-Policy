import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def create_bar_chart(df: pd.DataFrame, variable: str):
    if variable == "principles":
        df = df.iloc[0:4]
    elif variable == "pipeline":
        df = df.iloc[4:]
    else: 
        print("You wrote the wrong variable name!")
        return
    print(df)
    plt.figure(figsize=(15, 6))
    plt.bar(x = df["RQ1 variable"], height = df["Count of appearances"])
    plt.xticks(rotation=0, wrap=True)

    # add title and labels
    plt.title('RQ1: Distribution of categories of ethics')
    plt.ylabel('Count')

    # Show the plot
    #plt.tight_layout()
    plt.show()