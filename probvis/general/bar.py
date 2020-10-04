import os

import matplotlib.pyplot as plt
import seaborn as sns

from probvis.aux import save_fig

import numpy as np

def bar_plot(y, **args):
    y_label = args['y_label'] if 'y_label' in args else ''
    x_label = args['x_label'] if 'x_label' in args else ''
    x = args['x'] if 'x' in args else np.arange(0, len(y))
    title = args['title'] if 'title' in args else ''

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    color = args['color'] if 'color' in args else None
    y_lim = args['y_lim'] if 'y_lim' in args else None
    x_ticklabels = args['x_ticklabels'] if 'x_ticklabels' in args else x


    close = args['close'] if 'close' in args else 'all'
    rotation = args['rotation'] if 'rotation' in args else 0
    orient = args['orient'] if 'orient' in args else 'v'

    ticksize = args['ticksize'] if 'ticksize' in args.keys() else fontsize

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=(15, 10))
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    # bar_list = sns.barplot(x=x, y=y, orient=orient, ax=ax)
    if orient == 'v':
        bar_list = ax.bar(x=x, height=y, color=color)
        ax.set_xticks(x)
        ax.set_xticklabels(x_ticklabels)
        if y_lim: ax.set_ylim(y_lim)
    else:
        bar_list = ax.barh(y=x, width=y, color=color)
        ax.set_yticks(x)
        ax.set_yticklabels(x_ticklabels)
        if y_lim: ax.set_xlim(y_lim)
        ax.invert_yaxis()
    # if color:
    #     for i, c in enumerate(color):
    #         bar_list[i].set_color(c)



    ax.set_ylabel(y_label, fontsize=fontsize)
    ax.set_xlabel(x_label, fontsize=fontsize)
    ax.tick_params(axis='both', which='major', labelsize=ticksize)
    ax.set_title(title, fontsize=fontsize)


    if rotation >0:
        plt.xticks(rotation=rotation)


    x_ticks = []

    locs, labels = plt.xticks()
    # for i, tick in enumerate(ax.get_xticks()):
    #     x_ticks.append(str(tick) if i % 10 == 0 else '')
    # plt.xticks(locs, x_ticks)  # , rotation=45, horizontalalignment='right')

    ax.grid(True)
    if 'tight' in args: f.tight_layout()

    if close != -1: plt.close(close)

    return f, ax



def stacked_bar_plot(y_list, x_list, label_list, **args):
    ax, f = None, None

    for idx, (y, x) in enumerate(zip(y_list, x_list)):
        if idx == 0:
            ax, f = bar_plot(y=y, x=x)
        else:
            bar_plot(y=y, x=x, ax=ax)



    return ax, f
