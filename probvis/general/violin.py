
import seaborn as sns
import numpy as np
import os

import matplotlib.pyplot as plt

from probvis.aux import save_fig
import pandas as pd




def violin_plot(x_list, y_list, **args):
    log = args['log'] if 'log' in args else False
    showmeans = args['showmeans'] if 'showmeans' in args else False
    showmedians = args['showmedians'] if 'showmedians' in args else False

    color_list = args['color_list'] if 'color_list' in args else None

    xlabel = args['x_label'] if 'x_label' in args else ''
    ylabel = args['y_label'] if 'y_label' in args else ''
    title = args['title'] if 'title' in args else ''

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    close = args['close'] if 'close' in args else 'all'

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=(15, 10))
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']



    parts = ax.violinplot(y_list, showmeans=False, showextrema=False)

    if color_list:
        for i, b in enumerate(parts['bodies']):
            b.set_color(color_list[i])

    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(x_list) + 1))
    ax.set_xticklabels(x_list)
    ax.set_xlim(0.25, len(x_list) + 0.75)


    inds = np.arange(1, len(x_list)+1)
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
    # f.tight_layout()
    ax.tick_params(axis='both', which='major', labelsize=fontsize)
    ax.grid(True)
    if close != -1: plt.close(close)
    return f, ax



def violin2_plot(x_list, y_list, **args):

    xlabel = args['xlabel'] if 'xlabel' in args else 'x'
    ylabel = args['ylabel'] if 'ylabel' in args else ''
    title = args['title'] if 'title' in args else ''
    x_lim = args['x_lim'] if 'x_lim' in args else None

    showmeans = args['showmeans'] if 'showmeans' in args else False
    showmedians = args['showmedians'] if 'showmedians' in args else False
    quartiles = args['quartiles'] if 'quartiles' in args else []


    fontsize = args['fontsize'] if 'fontsize' in args else 32
    figsize = args['figsize'] if 'figsize' in args else (15,10)
    color_list = args['color_list'] if 'color_list' in args else None
    close = args['close'] if 'close' in args else 'all'

    name = '{}_'.format(args['name']) if 'name' in args else ''
    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=figsize)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    #%%

    parts = ax.violinplot(data_list, showmeans=False, showmedians=showmedians, showextrema=False)
    if color_list:
        for i, b in enumerate(parts['bodies']):
            b.set_color(color_list[i])

    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(label_list) + 1))
    ax.set_xticklabels(label_list)
    ax.set_xlim(0.25, len(label_list) + 0.75)


    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)
    if x_lim is not None:
        ax.set_xlim(x_lim)
    else:
        ax.set_xlim(0.25, len(label_list) + 0.75)

    inds = np.arange(1, len(label_list) + 1)
    min_max_data = np.percentile(data_list, [0,100], axis=-1)
    ax.vlines(inds, *min_max_data, color='k', linestyle='-', lw=1)
    if showmeans:
        means = np.mean(data_list, axis=-1)

        ax.scatter(inds, means, marker='o', color='white', s=30, zorder=3)

    if len(quartiles) == 2:
        quart_data = np.percentile(data_list, quartiles, axis=-1)

        ax.vlines(inds, *quart_data, color='k', linestyle='-', lw=5)

    # f.tight_layout()
    ax.tick_params(axis='both', which='major', labelsize=fontsize)
    ax.grid(True)

    if f is not None: save_fig(f, os.path.join(save_dir, f'{name}violin'))
    if close != -1: plt.close(close)
    return ax
