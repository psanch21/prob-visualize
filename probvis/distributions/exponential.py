import matplotlib.pyplot as plt
import os
import numpy as np
def plot_params(params, save_dir, name, title='', close=None):


    f = plt.figure(figsize=(15,10))
    x = np.arange(len(params))
    ax = plt.subplot(1, 1, 1)
    # ax.plot(params)
    ax.stem(x, params, use_line_collection=True)
    ax.set_title(title)

    f.savefig(os.path.join(save_dir, '{}_exp_params.png'.format(name)))

    if close != -1: plt.close(close)
    return f
