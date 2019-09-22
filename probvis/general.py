import matplotlib.pyplot as plt
import os
from probvis.aux import save_fig
import probvis.images as pvi
import numpy as np


def mean_var_plot(save_dir, x, name='',  xlabel='x', ylabel='y', close=None):
    n_samples, dim = x.shape
    mean = np.mean(x, axis=0)
    var  = np.var(x, axis=0)
    x_range = list(range(dim))
    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    ax.plot(x_range, mean, 'o', label='mean')
    ax.plot(x_range, var, 'o', label='var')

    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)

    if name is not '': name += '_'
    save_fig(f, os.path.join(save_dir, '{}mean_var'.format(name)))
    if close != -1: plt.close(close)



def hist_plot( x, label=None, density=False, logy=False, alpha=1.0, ax=None):
    n_samples = len(x)
    bins = min(30, int(np.sqrt(n_samples)))
    if label is not None:
        ax.hist(x, density=density, label=label, alpha=alpha, bins=bins)
    else:
        ax.hist(x, density=density, alpha=alpha, bins=bins)

    if logy: ax.set_yscale('log')



def multi_hist_plot(save_dir, data_list, label_list, name='', xlabel='x', density=False, logy=False, alpha=1.0,fontsize=18, close=None):
    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    for x, l in zip(data_list, label_list):
        hist_plot(x, l, density=density, logy=logy,  alpha=alpha, ax=ax)

    ax.set_xlabel(xlabel, fontsize=fontsize)
    f.tight_layout()
    ax.legend(fontsize=22)
    ax.tick_params(axis='both', which='major', labelsize=16)
    if name is not '': name += '_'
    save_fig(f, os.path.join(save_dir, '{}hist'.format(name)))
    if close != -1: plt.close(close)






def scater_plot(save_dir, x_data, y_data, name='', alpha=1.0,  xlabel='x', ylabel='y', close=None):
    assert len(x_data) == len(y_data)

    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    ax.scatter(x_data, y_data, alpha=alpha)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)

    if name is not '': name += '_'
    save_fig(f, os.path.join(save_dir, '{}scatter'.format(name)))
    if close != -1: plt.close(close)




def scater_plot_with_images(save_dir, x_data, y_data, images, name='', alpha=1.0,  xlabel='x', ylabel='y', close=None):
    assert len(x_data) == len(y_data)
    assert len(x_data) == len(images)

    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    ax.scatter(x_data, y_data, alpha=alpha)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)

    pvi.scatter_images(x_data, y_data, images, ax)

    if name is not '': name += '_'
    save_fig(f, os.path.join(save_dir, '{}scatter_im'.format(name)))
    if close != -1: plt.close(close)




