import os

import matplotlib.pyplot as plt
import seaborn as sns

from probvis.aux import save_fig

import numpy as np

def bar_plot(y, **args):
    y_label = args['y_label'] if 'y_label' in args else 'y'
    x_label = args['x_label'] if 'x_label' in args else 'x'
    x = args['x'] if 'x' in args else np.arange(0, len(y))
    title = args['title'] if 'title' in args else ''

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    close = args['close'] if 'close' in args else 'all'
    rotation = args['rotation'] if 'rotation' in args else 0
    orient = args['orient'] if 'orient' in args else 'v'

    ticksize = args['ticksize'] if 'ticksize' in args.keys() else 12

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=(15, 10))
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    sns.barplot(x=x, y=y, orient=orient, ax=ax)
    ax.set_ylabel(y_label, fontsize=fontsize)
    ax.set_xlabel(x_label, fontsize=fontsize)
    ax.tick_params(axis='x', which='major', labelsize=ticksize)
    ax.set_title(title)

    if rotation != 0:
        plt.xticks(rotation=90)


    x_ticks = []

    locs, labels = plt.xticks()
    # for i, tick in enumerate(ax.get_xticks()):
    #     x_ticks.append(str(tick) if i % 10 == 0 else '')
    # plt.xticks(locs, x_ticks)  # , rotation=45, horizontalalignment='right')

    ax.grid(True)
    if 'tight' in args: f.tight_layout()

    if close != -1: plt.close(close)

    return ax, f



def stacked_bar_plot(y_list, x_list, label_list, **args):
    ax, f = None, None

    for idx, (y, x) in enumerate(zip(y_list, x_list)):
        if idx == 0:
            ax, f = bar_plot(y=y, x=x)
        else:
            bar_plot(y=y, x=x, ax=ax)



    return ax, f
