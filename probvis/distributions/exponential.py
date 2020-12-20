import os

import matplotlib.pyplot as plt
import numpy as np

from probvis.aux import save_fig


def plot_params(params, save_dir, name, title='', close='all'):
    f = plt.figure(figsize=Cte.FIGSIZE)
    x = np.arange(len(params))
    ax = plt.subplot(1, 1, 1)
    # ax.plot(params)
    ax.stem(x, params, use_line_collection=True)
    ax.set_title(title)

    save_fig(f, os.path.join(save_dir, '{}_exp_params'.format(name)))

    if close != -1: plt.close(close)
    return f
