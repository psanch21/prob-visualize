import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from probvis.aux import save_fig



def radar_plot(y_list, label_list, **args):


    color = args['color'] if 'color' in args else None

    xlabel = args['x_label'] if 'x_label' in args else ''
    ylabel = args['y_label'] if 'y_label' in args else ''
    title = args['title'] if 'title' in args else ''

    alpha = args['alpha'] if 'alpha' in args else 0.25
    linewidth = args['linewidth'] if 'linewidth' in args else 2

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    fontsize_title =  args['fontsize_title'] if 'fontsize_title' in args else fontsize
    fontsize_ticks = args['fontsize_ticks'] if 'fontsize_ticks' in args else {'x': fontsize, 'y': fontsize}

    pad = args['pad'] if 'pad' in args else 0

    x_lim = args['x_lim'] if 'x_lim' in args else None
    y_lim = args['y_lim'] if 'y_lim' in args else None

    close = args['close'] if 'close' in args else 'all'
    tight = args['tight'] if 'tight' in args else None

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=(15, 10))
        ax = plt.subplot(1, 1, 1, polar=True)
    else:
        ax = args['ax']

    angles = np.linspace(0, 2 * np.pi, len(label_list), endpoint=False)

    angles = np.concatenate((angles, [angles[0]]))

    y_list = np.concatenate((y_list, [y_list[0]]))

    ax.plot(angles, y_list, 'o-', linewidth=linewidth, color=color)
    ax.fill(angles, y_list, alpha=alpha, color=color)
    ax.set_thetagrids(angles * 180 / np.pi, label_list)

    if x_lim:
        ax.set_xlim(x_lim)

    if y_lim is not None:
        ax.set_ylim(y_lim)


    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize_title, pad=pad)

    if 'x' in fontsize_ticks: ax.tick_params(axis='x', which='major', labelsize=fontsize_ticks['x'])
    if 'y' in fontsize_ticks: ax.tick_params(axis='y', which='major', labelsize=fontsize_ticks['y'])
    ax.grid(True)
    if close != -1: plt.close(close)
    if tight and f: f.tight_layout()
    return f, ax
