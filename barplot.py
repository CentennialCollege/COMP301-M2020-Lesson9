import matplotlib.pyplot as plt

import numpy as np

import random
from numpy.core.numeric import True_

import seaborn as sns


def SixSidedDie_BarPlot(number_of_rolls, seed=45):
    random.seed(seed)
    rolls = [random.randrange(1, 7) for i in range(number_of_rolls)]

    values, frequencies = np.unique(rolls, return_counts=True)

    #print(f'values: {values}, frequencies {frequencies}')

    #set up and configure our bar plot
    title = f'Rolling a Six-Sided    Die {len(rolls):,}       Times'
    sns.set_style('whitegrid')
    axes = sns.barplot(x=values, y=frequencies, palette='bright')

    #labelling the barplot axes and sets up the y limit
    axes.set_title(title)
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.20)

    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0                            # x coordinate where the text will appear -> calculates the center of each bar
        text_y = bar.get_height()                                               # y coordinate where the text will appear
        text = f'{frequency:,}\n{frequency / len(rolls):.3%}'                   # will print the frequency and distribution for each bar
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')  #show the text for each bar

    #displays the barplot
    plt.show()