

def hist_plot_i(x, label=None, color=None, density=False, logy=False, bins=None, alpha=1.0, ax=None):
    n_samples = len(x)
    if bins is None: bins = min(30, int(np.sqrt(n_samples)))
    if label is not None:
        ax.hist(x, density=density, label=label, alpha=alpha, bins=bins, color=color)
    else:
        ax.hist(x, density=density, alpha=alpha, bins=bins, color=color)

    if logy: ax.set_yscale('log')


def hist_plot(save_dir, x, **args):
    n_samples = len(x)

    label = args['label'] if 'label' in args else None
    density = args['density'] if 'density' in args else False

    logy = args['logy'] if 'logy' in args else False
    bins = args['bins'] if 'bins' in args else min(30, int(np.sqrt(n_samples)))
    alpha = args['alpha'] if 'alpha' in args else 1.0

    xlabel = args['xlabel'] if 'xlabel' in args else 'x'
    ylabel = args['ylabel'] if 'ylabel' in args else ''

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    close = args['close'] if 'close' in args else 'all'

    name = '{}_'.format(args['name']) if 'name' in args else ''


    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    if label is not None:
        ax.hist(x, density=density, label=label, alpha=alpha, bins=bins)
    else:
        ax.hist(x, density=density, alpha=alpha, bins=bins)

    if logy: ax.set_yscale('log')

    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    # f.tight_layout()
    ax.tick_params(axis='both', which='major', labelsize=32)
    ax.grid(True)
    if label is not None:
        ax.legend(fontsize=32, frameon=True)

    save_fig(f, os.path.join(save_dir, '{}hist'.format(name)))
    if close != -1: plt.close(close)

import matplotlib.pyplot as plt
import os
from probvis.aux import save_fig
import probvis.images as pvi
import numpy as np


def multi_hist_plot(save_dir, data_list, label_list, name='', color_list=None, xlabel='x', ylabel='', density=False,
                    logy=False, alpha=1.0, fontsize=32, close='all', binwidth=None, x_lim=None):
    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    if binwidth is None:
        min_list = [np.min(d) for d in data_list]
        max_list = [np.max(d) for d in data_list]
        binwidth = (np.max(max_list) - np.min(min_list)) / (np.sqrt(len(data_list[0])) * 0.8)

    i = 0
    for x, l in zip(data_list, label_list):
        if color_list is None:
            hist_plot_i(x, l, density=density, logy=logy, alpha=alpha, ax=ax,
                        bins=np.arange(min(x), max(x) + binwidth, binwidth))
        else:
            hist_plot_i(x, l, density=density, logy=logy, alpha=alpha, ax=ax,
                        bins=np.arange(min(x), max(x) + binwidth, binwidth), color=color_list[i])
        i += 1
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    if x_lim is not None:
        ax.set_xlim(x_lim)
    # f.tight_layout()
    ax.legend(fontsize=fontsize, frameon=False)
    ax.tick_params(axis='both', which='major', labelsize=32)
    ax.grid(True)
    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}hist'.format(name)))
    if close != -1: plt.close(close)
