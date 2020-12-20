
from sklearn.neighbors import KernelDensity
import numpy as np
import os

import matplotlib.pyplot as plt

from probvis.aux import save_fig


import probvis.aux as pva

from probvis.aux import Cte
def kde_plot(x, **args):

    label = args['label'] if 'label' in args else None

    n_points = args['n_points'] if 'n_points' in args else 1000
    bandwidth = args['bandwidth'] if 'bandwidth' in args else 1.0
    kernel = args['kernel'] if 'kernel' in args else 'gaussian'

    x_label = args['x_label'] if 'x_label' in args else ''
    y_label = args['y_label'] if 'y_label' in args else ''
    title = args['title'] if 'title' in args else ''
    x_lim = args['x_lim'] if 'x_lim' in args else None
    color = args['color'] if 'color' in args else 'darkblue'
    log_axis = args['log_axis'] if 'log_axis' in args else []
    fill = args['fill'] if 'fill' in args else True


    fontsize = args['fontsize'] if 'fontsize' in args else None
    close = args['close'] if 'close' in args else 'all'
    pad = args['pad'] if 'pad' in args else 0
    k_pos = args['k_pos'] if 'k_pos' in args else 0.01

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=Cte.FIGSIZE)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    #%%

    kde = KernelDensity(bandwidth=bandwidth, kernel=kernel)
    kde.fit(x[:, None])
    x_d = np.linspace(x.min(), x.max(), n_points)
    # score_samples returns the log of the probability density
    logprob = kde.score_samples(x_d[:, None])
    if fill:
        if label:
            ax.fill_between(x_d, np.exp(logprob), alpha=0.5, label=label, color=color)
        else:
            ax.fill_between(x_d, np.exp(logprob), alpha=0.5)
    else:
        if label is not None:
            ax.plot(x_d, np.exp(logprob), color=color, label=label)
        else:
            ax.plot(x_d, np.exp(logprob),  color=color)

    ax.plot(x, np.full_like(x, -k_pos), '|k', markeredgewidth=1, color=color)


    ax.set_xlabel(x_label, fontsize=fontsize)
    ax.set_ylabel(y_label, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)

    if x_lim is not None: ax.set_xlim(x_lim)

    if 'y' in log_axis: ax.set_yscale('log')
    if 'x' in log_axis: ax.set_xscale('log')

    # f.tight_layout()
    ax.tick_params(axis='both', which='major', labelsize=fontsize)
    ax.grid(True)
    # ax.legend(fontsize=32, frameon=True)

    if close != -1: plt.close(close)
    return ax, f
