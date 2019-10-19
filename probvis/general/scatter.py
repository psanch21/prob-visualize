import os

import matplotlib.pyplot as plt
import numpy as np

import probvis.images as pvi
from probvis.aux import save_fig


def scatter_plot(save_dir, x_data, y_data, name='', alpha=1.0, xlabel='x', ylabel='y', close='all'):
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


def scatter_plot_list(save_dir, x_list, y_list, color_list, label_list, name='', xlabel='x', ylabel='y', close='all',
                      **args):
    fontsize = args['fontsize'] if 'fontsize' in args.keys() else 32
    ticksize = args['ticksize'] if 'ticksize' in args.keys() else 18
    alpha = args['alpha'] if 'alpha' in args.keys() else 1.0

    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    for x_data, y_data, color, label in zip(x_list, y_list, color_list, label_list):
        ax.scatter(x_data, y_data, alpha=alpha, label=label, color=color)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)

    ax.grid(True)

    ax.legend(fontsize=fontsize, frameon=True)
    ax.tick_params(axis='both', which='major', labelsize=ticksize)
    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}scatter_l'.format(name)))
    if close != -1: plt.close(close)


def scater_plot_cluster(save_dir, x_data, y_data, label, label_id, color, marker, name='', alpha=1.0, xlabel='x',
                        ylabel='y', close='all', x_lim=[0.0, 1.0], y_lim=[0.0, 1.0], islegend=True):
    assert len(x_data) == len(y_data)

    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    for i in range(len(x_data)):
        ax.scatter(x_data[i], y_data[i], label=label[i], marker=marker[label_id[i]], s=256, alpha=alpha,
                   color=color[label_id[i]])

    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)

    ax.tick_params(axis='both', which='major', labelsize=32)

    ax.grid(True)
    # f.tight_layout()

    handles, labels = ax.get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)

    idx = np.argsort(label_list)
    label_list = [label_list[i] for i in idx]
    handle_list = [handle_list[i] for i in idx]
    if islegend:
        ax.legend(handle_list, label_list, fontsize=32, frameon=False, ncol=1, handlelength=4)
        ax.set_xlabel(xlabel, fontsize=32)
        ax.set_ylabel(ylabel, fontsize=32)

    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}scatter_clus'.format(name)))
    if close != -1: plt.close(close)


def scatter_plot_with_images(save_dir, x_data, y_data, images, name='', alpha=1.0, xlabel='x', ylabel='y', close='all'):
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
