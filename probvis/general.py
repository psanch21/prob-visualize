import matplotlib.pyplot as plt
import os
from probvis.aux import save_fig
import probvis.images as pvi
import numpy as np
import seaborn as sns
#%% Plot

def mean_var_plot(save_dir, x, name='',  xlabel='x', ylabel='y', close='all'):
    n_samples, dim = x.shape
    mean = np.mean(x, axis=0)
    var  = np.var(x, axis=0)
    x_range = list(range(dim))
    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    ax.plot(x_range, mean, 'o', label=r'$\mu$')
    ax.plot(x_range, var, 'o', label=r'$\sigma^2$')

    ax.legend(fontsize=32, frameon=True, ncol=2, handlelength=4, loc='center')
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_xlabel(xlabel, fontsize=32)
    ax.set_ylabel(ylabel, fontsize=32)

    ax.grid(True)
    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}mean_var'.format(name)))
    if close != -1: plt.close(close)


#%% Hist


def hist_plot( x, label=None, density=False, logy=False, alpha=1.0, ax=None):
    n_samples = len(x)
    bins = min(30, int(np.sqrt(n_samples)))
    if label is not None:
        ax.hist(x, density=density, label=label, alpha=alpha, bins=bins)
    else:
        ax.hist(x, density=density, alpha=alpha, bins=bins)

    if logy: ax.set_yscale('log')



def multi_hist_plot(save_dir, data_list, label_list, name='', xlabel='x', density=False, logy=False, alpha=1.0,fontsize=32, close='all'):
    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    for x, l in zip(data_list, label_list):
        hist_plot(x, l, density=density, logy=logy,  alpha=alpha, ax=ax)

    ax.set_xlabel(xlabel, fontsize=fontsize)
    f.tight_layout()
    ax.legend(fontsize=32, frameon=False)
    ax.tick_params(axis='both', which='major', labelsize=32)
    ax.grid(True)
    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}hist'.format(name)))
    if close != -1: plt.close(close)




#%% Scatter


def scater_plot(save_dir, x_data, y_data,name='', alpha=1.0,  xlabel='x', ylabel='y', close='all'):
    assert len(x_data) == len(y_data)


    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    ax.scatter(x_data, y_data, alpha=alpha)
    ax.set_xlabel(xlabel, fontsize=18)
    ax.set_ylabel(ylabel, fontsize=18)

    ax.grid(True)

    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}scatter'.format(name)))
    if close != -1: plt.close(close)

def scater_plot_cluster(save_dir, x_data, y_data,label, label_id, color, marker, name='', alpha=1.0,  xlabel='x', ylabel='y', close='all', x_lim=[0.0, 1.0], y_lim=[0.0, 1.0]):
    assert len(x_data) == len(y_data)

    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    for i in range(len(x_data)):
        ax.scatter(x_data[i], y_data[i], label=label[i], marker=marker[label_id[i]], s=256, alpha=alpha, color=color[label_id[i]])
    ax.set_xlabel(xlabel, fontsize=32)
    ax.set_ylabel(ylabel, fontsize=32)

    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)

    ax.tick_params(axis='both', which='major', labelsize=16)

    ax.grid(True)
    f.tight_layout()

    handles, labels = ax.get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)

    idx = np.argsort(label_list)
    label_list = [ label_list[i] for i in idx]
    handle_list = [handle_list[i] for i in idx]
    ax.legend(handle_list, label_list, fontsize=18, frameon=False, ncol=2,handlelength=4)


    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}scatter_clus'.format(name)))
    if close != -1: plt.close(close)





def scater_plot_with_images(save_dir, x_data, y_data, images, name='', alpha=1.0,  xlabel='x', ylabel='y', close='all'):
    assert len(x_data) == len(y_data), 'x_data {} y_data {} images {}'.format(len(x_data), len(y_data), len(images))
    assert len(x_data) == len(images)

    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    ax.scatter(x_data, y_data, alpha=alpha)
    ax.set_xlabel(xlabel, fontsize=32)
    ax.set_ylabel(ylabel, fontsize=32)

    pvi.scatter_images(x_data, y_data, images, ax)

    ax.tick_params(axis='both', which='major', labelsize=16)

    ax.grid(True)
    # f.tight_layout()

    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}scatter_im'.format(name)))
    if close != -1: plt.close(close)





#%% Box plot


def box_plot(save_dir, df,x_col, y_col, label_order, x_tick_label, name='',  xlabel='', ylabel='y', close='all'):


    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)
    ax.grid(True)
    ax = sns.boxplot(x=x_col, y=y_col, order=label_order, data=df, ax=ax)
    ax.set_xlabel(xlabel)  #
    ax.set_ylabel(ylabel, fontsize=32)#
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_xticklabels(x_tick_label, fontsize=32)
    f.tight_layout()

    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}box'.format(name)))
    if close != -1: plt.close(close)


