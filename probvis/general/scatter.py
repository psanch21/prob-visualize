import os

import matplotlib.pyplot as plt
import numpy as np

import probvis.images as pvi
from probvis.aux import save_fig
import statsmodels.api as sm



def scatter_plot(x_data, y_data,  **args):
    assert len(x_data) == len(y_data)

    y_label = args['y_label'] if 'y_label' in args else 'y'
    y_ticks = args['y_ticks'] if 'y_ticks' in args else None
    x_label = args['x_label'] if 'x_label' in args else 'x'
    x_ticks = args['x_ticks'] if 'x_ticks' in args else None
    log_axis = args['log_axis'] if 'log_axis' in args else []
    fontsize = args['fontsize'] if 'fontsize' in args else 32
    ticksize = args['ticksize'] if 'ticksize' in args else fontsize
    title = args['title'] if 'title' in args else ''
    title_stats = args['title_stats'] if 'title_stats' in args else False

    alpha = args['alpha'] if 'alpha' in args else 1.0

    close = args['close'] if 'close' in args else 'all'

    figsize = args['figsize'] if 'figsize' in args else (15, 10)

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=figsize)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    ax.scatter(x_data, y_data, alpha=alpha)

    ax.set_ylabel(y_label, fontsize=fontsize)
    ax.set_xlabel(x_label, fontsize=fontsize)
    ax.set_title(title)

    if title_stats:
        if 'y' in log_axis: y_data = np.log(y_data)
        if 'x' in log_axis: x_data = np.log(x_data)

        model1 = sm.OLS(y_data, x_data)

        result = model1.fit()
        ax.set_title(f'p-value: {result.pvalues[0]:0.3f} F p-value: {result.f_pvalue:0.3f} R2: {result.rsquared*100:0.2f}  R2 a: {result.rsquared_adj*100:0.2f}')

    if 'y' in log_axis: ax.set_yscale('log')
    if 'x' in log_axis: ax.set_xscale('log')

    ax.tick_params(axis='both', which='major', labelsize=ticksize)

    ax.grid(True)

    if close != -1: plt.close(close)
    return f, ax


def scatter_plot_list(x_list, y_list, color_list, label_list,
                      **args):
    fontsize = args['fontsize'] if 'fontsize' in args.keys() else 32
    ticksize = args['ticksize'] if 'ticksize' in args.keys() else 18
    alpha = args['alpha'] if 'alpha' in args.keys() else 1.0

    y_label = args['y_label'] if 'y_label' in args else ''
    x_label = args['x_label'] if 'x_label' in args else ''
    log_axis = args['log_axis'] if 'log_axis' in args else []

    close = args['close'] if 'close' in args else 'all'



    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    for x_data, y_data, color, label in zip(x_list, y_list, color_list, label_list):
        ax.scatter(x_data, y_data, alpha=alpha, label=label, color=color)
    ax.set_xlabel(y_label, fontsize=fontsize)
    ax.set_ylabel(x_label, fontsize=fontsize)

    if 'y' in log_axis: ax.set_yscale('log')
    if 'x' in log_axis: ax.set_xscale('log')

    ax.grid(True)

    ax.legend(fontsize=fontsize, frameon=True)
    ax.tick_params(axis='both', which='major', labelsize=ticksize)

    if close != -1: plt.close(close)

    return f, ax


def scatter_plot_cluster(x_data, y_data, label, label_id, color_list, marker_list, **args):
    assert len(x_data) == len(y_data)

    fontsize = args['fontsize'] if 'fontsize' in args.keys() else 32
    ticksize = args['ticksize'] if 'ticksize' in args.keys() else 18
    alpha = args['alpha'] if 'alpha' in args.keys() else 1.0

    y_label = args['y_label'] if 'y_label' in args else ''
    x_label = args['x_label'] if 'x_label' in args else ''

    x_lim = args['x_lim'] if 'x_lim' in args else None
    y_lim = args['y_lim'] if 'y_lim' in args else None

    islegend = args['islegend'] if 'islegend' in args else True

    log_axis = args['log_axis'] if 'log_axis' in args else []

    close = args['close'] if 'close' in args else 'all'


    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    for i in range(len(x_data)):
        ax.scatter(x_data[i], y_data[i], label=label[i], marker=marker_list[label_id[i]], s=256, alpha=alpha,
                   color=color_list[label_id[i]])

    if x_lim: ax.set_xlim(x_lim)
    if y_lim: ax.set_ylim(y_lim)

    if 'y' in log_axis: ax.set_yscale('log')
    if 'x' in log_axis: ax.set_xscale('log')

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
        ax.set_xlabel(x_label, fontsize=32)
        ax.set_ylabel(y_label, fontsize=32)

    if close != -1: plt.close(close)

    return f, ax


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
