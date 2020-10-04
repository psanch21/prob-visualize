from probvis.aux import save_fig
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.ticker import FixedFormatter

import numpy as np
def heatmap_plot(matrix, **args):
    y_label = args['y_label'] if 'y_label' in args else ''
    y_ticks = args['y_ticks'] if 'y_ticks' in args else None
    x_ticks = args['x_ticks'] if 'x_ticks' in args else None
    x_label = args['x_label'] if 'x_label' in args else ''

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    close = args['close'] if 'close' in args else 'all'
    title = args['title'] if 'title' in args else ''
    figsize = args['figsize'] if 'figsize' in args else (15, 10)

    vmin = args['vmin'] if 'vmin' in args else None
    vmax = args['vmax'] if 'vmax' in args else None

    annot = args['annot'] if 'annot' in args else None
    fmt = args['fmt'] if 'fmt' in args else None


    tight = args['tight'] if 'tight' in args else False

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=figsize)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']
    sns.heatmap(matrix, ax=ax, vmin=vmin, vmax=vmax, annot=annot, fmt=fmt)
    ax.set_ylabel(y_label,  fontsize=fontsize)
    ax.set_xlabel(x_label, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)

    ax.tick_params(axis='both', which='major', labelsize=16)
    if x_ticks is None: ax.set_xticklabels([])
    if y_ticks is not None: ax.set_yticklabels(y_ticks)

    if tight: f.tight_layout()

    if close != -1: plt.close(close)
    return f, ax


def heatmap_plot_cols(matrix, **args):
    y_label = args['y_label'] if 'y_label' in args else ''
    y_ticks = args['y_ticks'] if 'y_ticks' in args else None
    x_ticks = args['x_ticks'] if 'x_ticks' in args else None
    x_label = args['x_label'] if 'x_label' in args else ''

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    close = args['close'] if 'close' in args else 'all'
    title = args['title'] if 'title' in args else ''
    figsize = args['figsize'] if 'figsize' in args else (15, 10)

    vmin = args['vmin'] if 'vmin' in args else None
    vmax = args['vmax'] if 'vmax' in args else None

    cmap = args['cmap'] if 'cmap' in args else 'coolwarm'
    cbar = args['cbar'] if 'cbar' in args else False

    rotation_x = args['rotation_x'] if 'rotation_x' in args else 0

    annot = args['annot'] if 'annot' in args else None
    fmt = args['fmt'] if 'fmt' in args else None


    tight = args['tight'] if 'tight' in args else False


    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=figsize)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    b = np.argsort(np.argsort(matrix, axis=0), axis=0)

    im = ax.imshow(b, aspect="auto", cmap=cmap, vmin=vmin, vmax=vmax)
    if cbar:
        cbari = f.colorbar(im, ax=ax, ticks=np.array([0.0, 0.5, 1.0]) * b.max(),
                   format=FixedFormatter(["low", "middle", "high"]))
        cbari.ax.tick_params(labelsize=fontsize)
        # cbar.ax.set_yticklabels(ticklabs, fontsize=fontsize)
    if annot:
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                my_value = f'{ matrix[i, j]:{fmt}}'
                ax.text(j, i, my_value, ha="center", va="center", fontsize=fontsize)


    ax.set_ylabel(y_label,  fontsize=fontsize)
    ax.set_xlabel(x_label, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)

    ax.tick_params(axis='both', which='major', labelsize=fontsize)
    if x_ticks is not None:
        ax.set_xticks(np.arange(len(x_ticks)))
        ax.set_xticklabels(x_ticks, rotation=rotation_x)
    if y_ticks is not None:
        ax.set_yticks(np.arange(len(y_ticks)))
        ax.set_ylim(len(y_ticks) - 0.5, -0.5)

        ax.set_yticklabels(y_ticks)

    # ax.invert_yaxis()
    ax.xaxis.tick_top()

    if tight: f.tight_layout()

    if close != -1: plt.close(close)
    return f, ax

