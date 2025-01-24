import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import colormaps
import seaborn as sns
from matplotlib.ticker import MaxNLocator

def create_bar_chart(df: pd.DataFrame, variable: str, color: str):
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
    colors = color

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
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

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

# function that takes a dictionary to visualize counts from this
def create_descriptive_charts(df: pd.DataFrame):
    
    plt.rcParams["figure.figsize"]=(30, 12)
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["Lato"]
    plt.rcParams["font.size"] = 16

    # one use of matplotlib colors and another with seaborn
    colors = [plt.get_cmap("Accent").colors,
              plt.get_cmap("Set2").colors,
              plt.get_cmap("tab20").colors,
              plt.get_cmap("tab10").colors
            ]
    #colors = sns.color_palette("dark", desat=0.6, as_cmap=True)

    df = df
    cols = ["Language", "Publication year", "Publishing institution", "Document type"]
    year_ticks = range(2016, 2025)

    fig, axes = plt.subplots(2, 2, sharex=False, sharey=True)

    fig.suptitle("Document characteristics", fontsize=20)

    col = 0
    for i in range(0, 2):
        for j in range(0, 2):
            bars = axes[i][j].bar(x=df[cols[col]].value_counts().index, height=df[cols[col]].value_counts()[0:], color=colors[col])
            axes[i][j].set_title(cols[col])
            axes[i][j].set_ylabel("Count", labelpad=15)
            axes[i][j].spines['top'].set_visible(False)
            axes[i][j].spines['right'].set_visible(False)
            axes[i][j].spines['left'].set_visible(False)
            axes[i][j].spines['bottom'].set_color('#DDDDDD')
            axes[i][j].tick_params(axis="x", bottom=False, left=False)
            axes[i][j].set_axisbelow(True)
            axes[i][j].yaxis.grid(True, color='#EEEEEE')
            axes[i][j].xaxis.grid(False)
            # if col is 1 then we are on the year column and we need to manually set ticks here
            if col == 1:
                axes[i][j].set_xticks(year_ticks)
            elif col == 2 or col == 3:
                # get labels and linebreak them
                wrapped_labels = [label.get_text().replace(' ', '\n') for label in axes[i][j].get_xticklabels()]
                axes[i][j].set_xticklabels(wrapped_labels)
            for bar in bars:
                axes[i][j].text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 0.3, 
                    round(bar.get_height(), 1),
                    horizontalalignment="center",
                    color=bar.get_facecolor(),
                    weight="bold",
                )
                
            col += 1

    plt.tight_layout()
    #plt.show()
    filename = "descriptive_chart.pdf"
    plt.savefig(filename)