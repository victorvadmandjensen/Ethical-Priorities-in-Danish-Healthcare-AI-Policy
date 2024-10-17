import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import colormaps
import seaborn as sns

def create_bar_chart(df: pd.DataFrame, variable: str):
    if variable == "principles":
        df = df.iloc[0:5]
    elif variable == "pipeline":
        df = df.iloc[5:]
    else: 
        print("You wrote the wrong variable name!")
        return
    
    plt.rcParams["figure.figsize"]=(15, 7)
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["Lato"]
    plt.rcParams["font.size"] = 18

    # one use of matplotlib colors and another with seaborn
    #colors = plt.get_cmap("tab10").colors
    #colors = sns.color_palette("dark", desat=0.6, as_cmap=True)
    colors = "#EE7F00"

    fig, ax = plt.subplots()

    bars = ax.bar(
        x = df["RQ1 variable"], 
        height = df["Count of appearances"],
        width=0.5,
        color = colors
        )
    
    # create list of labels with linebreaks
    labels = df["RQ1 variable"].values
    wrapped_labels = [label.replace(' ', '\n') for label in labels ]

    # style axes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)

    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3, 
            round(bar.get_height(), 1),
            horizontalalignment="center",
            color=bar.get_facecolor(),
            weight="bold",
        )   

    ax.set_title('RQ1: Distribution of the ethics of healthcare AI across ' + variable, pad=15, weight="bold")
    ax.set_xlabel("Healthcare AI " + variable, labelpad=15)
    ax.set_ylabel("Count", labelpad=15)
    ax.set_xticklabels(wrapped_labels)


    plt.tight_layout()
    #plt.show()
    filename = "bar_chart_" + variable + ".pdf"
    plt.savefig(filename)
