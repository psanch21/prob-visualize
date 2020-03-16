
from sklearn.neighbors import KernelDensity
import numpy as np
import os

import matplotlib.pyplot as plt

from probvis.aux import save_fig




def kde_plot(save_dir, x, **args):

    label = args['label'] if 'label' in args else None

    n_points = args['n_points'] if 'n_points' in args else 1000
    bandwidth = args['bandwidth'] if 'bandwidth' in args else 1.0
    kernel = args['kernel'] if 'kernel' in args else 'gaussian'

    xlabel = args['xlabel'] if 'xlabel' in args else 'x'
    ylabel = args['ylabel'] if 'ylabel' in args else ''
    title = args['title'] if 'title' in args else ''


    fontsize = args['fontsize'] if 'fontsize' in args else 32
    close = args['close'] if 'close' in args else 'all'

    name = '{}_'.format(args['name']) if 'name' in args else ''
    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=(15, 10))
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    #%%

    kde = KernelDensity(bandwidth=bandwidth, kernel=kernel)
    kde.fit(x[:, None])
    x_d = np.linspace(x.min(), x.max(), n_points)
    # score_samples returns the log of the probability density
    logprob = kde.score_samples(x_d[:, None])
    ax.fill_between(x_d, np.exp(logprob), alpha=0.5)
    ax.plot(x, np.full_like(x, -0.01), '|k', markeredgewidth=1)


    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)
    # f.tight_layout()
    ax.tick_params(axis='both', which='major', labelsize=fontsize)
    ax.grid(True)
    if label is not None:
        ax.legend(fontsize=32, frameon=True)

    if f is not None: save_fig(f, os.path.join(save_dir, f'{name}kde'))
    if close != -1: plt.close(close)
    return ax
