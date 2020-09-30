import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from probvis.aux import save_fig



def pie_plot(size_list, label_list, **args):


    color_list = args['color_list'] if 'color_list' in args else None

    title = args['title'] if 'title' in args else ''

    explode = [args['explode'],]*len(size_list) if 'explode' in args else [0.0,]*len(size_list)

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    fontsize_title =  args['fontsize_title'] if 'fontsize_title' in args else fontsize
    fontsize_ticks = args['fontsize_ticks'] if 'fontsize_ticks' in args else {'x': fontsize, 'y': fontsize}

    pad = args['pad'] if 'pad' in args else 0
    shadow = args['shadow'] if 'shadow' in args else False

    close = args['close'] if 'close' in args else 'all'
    tight = args['tight'] if 'tight' in args else None

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=(15, 10))
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    ax.pie(size_list, explode=explode, labels=label_list, autopct='%1.1f%%', colors=color_list,
            shadow=shadow, startangle=90, textprops={'fontsize': fontsize})
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    ax.set_title(title, fontsize=fontsize_title, pad=pad)

    if 'x' in fontsize_ticks: ax.tick_params(axis='x', which='major', labelsize=fontsize_ticks['x'])
    if 'y' in fontsize_ticks: ax.tick_params(axis='y', which='major', labelsize=fontsize_ticks['y'])

    if close != -1: plt.close(close)
    if tight and f: f.tight_layout()
    return f, ax


