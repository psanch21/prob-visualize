import os

import matplotlib.pyplot as plt
import numpy as np
import probvis.aux as pva

from probvis.aux import save_fig
from probvis.aux import Cte

def hist_plot_i(x, label=None, color=None, density=False, logy=False, bins=None, alpha=1.0, ax=None):
    n_samples = len(x)
    if bins is None: bins = min(30, int(np.sqrt(n_samples)))
    if label is not None:
        _, bins, _ = ax.hist(x, density=density, label=label, alpha=alpha, bins=bins, color=color)
    else:
        _, bins, _ = ax.hist(x, density=density, alpha=alpha, bins=bins, color=color)

    if logy: ax.set_yscale('log')


def hist_plot(x, **args):
    n_samples = len(x)

    label = args['label'] if 'label' in args else None
    density = args['density'] if 'density' in args else False
    logy = args['logy'] if 'logy' in args else False
    logx = args['logx'] if 'logx' in args else False

    histtype = args['histtype'] if 'histtype' in args else 'bar'
    bins = args['bins'] if 'bins' in args else min(30, int(np.sqrt(n_samples)))

    if 'bins_list' in args:
        bins =  args['bins_list']
    alpha = args['alpha'] if 'alpha' in args else 1.0

    x_label = args['x_label'] if 'x_label' in args else ''
    y_label = args['y_label'] if 'y_label' in args else ''
    title = args['title'] if 'title' in args else ''

    fontsize = args['fontsize'] if 'fontsize' in args else None
    linewidth = args['linewidth'] if 'linewidth' in args else 0
    close = args['close'] if 'close' in args else 'all'
    rotate = args['rotate'] if 'rotate' in args else 0.0
    v_line = args['v_line'] if 'v_line' in args else None
    color = args['color'] if 'color' in args else pva.get_color(0)
    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=Cte.FIGSIZE)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']


    if logx:
        weights, bins = np.histogram(x, bins=bins)

        bins = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))


    ax.hist(x, density=density, label=label, alpha=alpha, bins=bins, color=color,
                histtype=histtype, linewidth=linewidth)

    if histtype != 'step' and linewidth>0:
        ax.hist(x, density=density,  bins=bins, color=color,
                histtype='step', linewidth=linewidth)


    if logy: ax.set_yscale('log')
    if logx: ax.set_xscale('log')


    ax.set_xlabel(x_label, fontsize=fontsize)
    ax.set_ylabel(y_label, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)
    # f.tight_layout()
    if rotate>0.0:
        plt.xticks(rotation=rotate)
    ax.tick_params(axis='both', which='major', labelsize=fontsize)
    ax.grid(True)
    if v_line is not None:
        plt.axvline(x=v_line, color='k', linestyle='--')
    if close != -1: plt.close(close)
    return f, ax







def multi_hist_plot(save_dir, data_list, label_list, **args):
    v_line = args['v_line'] if 'v_line' in args else None
    color_list = args['color_list'] if 'color_list' in args else None

    density = args['density'] if 'density' in args else False

    logy = args['logy'] if 'logy' in args else False
    binwidth = args['binwidth'] if 'binwidth' in args else None
    alpha = args['alpha'] if 'alpha' in args else 1.0

    xlabel = args['xlabel'] if 'xlabel' in args else 'x'
    ylabel = args['ylabel'] if 'ylabel' in args else ''
    x_lim = args['x_lim'] if 'x_lim' in args else None

    fontsize = args['fontsize'] if 'fontsize' in args else None
    close = args['close'] if 'close' in args else 'all'

    name = '{}_'.format(args['name']) if 'name' in args else ''

    f = plt.figure(figsize=Cte.FIGSIZE)
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

    if v_line is not None:
        plt.axvline(x=v_line, color='k', linestyle='--')
    save_fig(f, os.path.join(save_dir, '{}hist'.format(name)))
    if close != -1: plt.close(close)
    return f, ax
