import os

import matplotlib.pyplot as plt
import seaborn as sns

from probvis.aux import save_fig

import numpy as np

def bar_plot(save_dir, y, **args):
    y_label = args['y_label'] if 'y_label' in args else 'y'
    x_label = args['x_label'] if 'x_label' in args else 'x'
    x = args['x'] if 'x' in args else np.arange(0, len(y))
    title = args['title'] if 'title' in args else ''

    name = '{}_'.format(args['name']) if 'name' in args else ''
    fontsize = args['fontsize'] if 'fontsize' in args else 32
    close = args['close'] if 'close' in args else 'all'

    ticksize = args['ticksize'] if 'ticksize' in args.keys() else 12

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=(15, 10))
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']
    sns.barplot(x=x, y=y, ax=ax)
    ax.set_ylabel(y_label, fontsize=fontsize)
    ax.set_xlabel(x_label, fontsize=fontsize)
    ax.tick_params(axis='x', which='major', labelsize=ticksize)
    ax.set_title(title)


    x_ticks = []
    locs, labels = plt.xticks()
    # for i, tick in enumerate(ax.get_xticks()):
    #     x_ticks.append(str(tick) if i % 10 == 0 else '')
    # plt.xticks(locs, x_ticks)  # , rotation=45, horizontalalignment='right')

    ax.grid(True)
    if 'tight' in args: f.tight_layout()

    if f is not None: save_fig(f, os.path.join(save_dir, '{}bar'.format(name)))
    if close != -1: plt.close(close)
