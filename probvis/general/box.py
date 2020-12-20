import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from probvis.aux import save_fig
from probvis.aux import Cte

def box2_plot(save_dir, df, x_col, y_col, label_order, x_tick_label, name='', xlabel='', ylabel='y', close='all'):
    f = plt.figure(figsize=Cte.FIGSIZE)
    ax = plt.subplot(1, 1, 1)
    ax.grid(True)
    ax = sns.boxplot(x=x_col, y=y_col, order=label_order, data=df, ax=ax)
    ax.set_xlabel(xlabel)  #
    ax.set_ylabel(ylabel, fontsize=32)  #
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_xticklabels(x_tick_label, fontsize=32)
    f.tight_layout()

    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}box'.format(name)))
    if close != -1: plt.close(close)


def box_plot(x_list, y_list, **args):
    log = args['log'] if 'log' in args else False
    showmeans = args['showmeans'] if 'showmeans' in args else False

    color_list = args['color_list'] if 'color_list' in args else None

    xlabel = args['x_label'] if 'x_label' in args else ''
    ylabel = args['y_label'] if 'y_label' in args else ''
    title = args['title'] if 'title' in args else ''

    rotate = args['rotate'] if 'rotate' in args else 0

    fontsize = args['fontsize'] if 'fontsize' in args else None
    close = args['close'] if 'close' in args else 'all'

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=Cte.FIGSIZE)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    df = pd.DataFrame(columns=['x', 'y'])

    for x, y in zip(x_list, y_list):
        d = {'x': [x, ] * len(y), 'y': y}
        df_tmp = pd.DataFrame(d)
        df = df.append(df_tmp)

    parts = sns.boxplot(x=df['x'], y=df['y'], ax=ax, showmeans=False)

    if color_list:
        for i, b in enumerate(parts['bodies']):
            b.set_color(color_list[i])

    inds = np.arange(0, len(x_list))
    if isinstance(showmeans, dict):
        means = [np.mean(y) for y in y_list]
        if 'marker' not in showmeans: showmeans['marker'] = 'o'
        if 'color' not in showmeans: showmeans['color'] = 'black'
        if 's' not in showmeans: showmeans['s'] = 30
        if 'zorder' not in showmeans: showmeans['zorder'] = 3

        ax.scatter(inds, means, **showmeans)

    if log: ax.set_yscale('log')

    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)

    if rotate>0:
        plt.xticks(rotation=rotate)

    # f.tight_layout()
    ax.tick_params(axis='both', which='major', labelsize=fontsize)
    ax.grid(True)
    if close != -1: plt.close(close)
    return f, ax



def box_plot_from_df(df, x, y,  **args):
    log = args['log'] if 'log' in args else False
    hue = args['hue'] if 'hue' in args else None
    showmeans = args['showmeans'] if 'showmeans' in args else False

    color_list = args['color_list'] if 'color_list' in args else None

    xlabel = args['x_label'] if 'x_label' in args else ''
    ylabel = args['y_label'] if 'y_label' in args else ''
    title = args['title'] if 'title' in args else ''

    rotate = args['rotate'] if 'rotate' in args else 0

    fontsize = args['fontsize'] if 'fontsize' in args else None
    close = args['close'] if 'close' in args else 'all'
    grid = args['grid'] if 'grid' in args else True

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=Cte.FIGSIZE)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']


    parts = sns.boxplot(x=x, y=y, hue=hue, data=df, ax=ax, showmeans=showmeans)


    if log: ax.set_yscale('log')

    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)

    if rotate>0:
        plt.xticks(rotation=rotate)

    # f.tight_layout()
    ax.tick_params(axis='both', which='major', labelsize=fontsize)
    if grid: ax.grid(True)
    if close != -1: plt.close(close)
    return f, ax
