import os

import matplotlib.pyplot as plt
import numpy as np

from probvis.aux import save_fig, get_color


# %% Plot

def multi_simple_plot(save_dir, y_list, label_list, **args):
    y_label = args['y_label'] if 'y_label' in args else 'y'
    x_label = args['x_label'] if 'x_label' in args else 'x'
    name = '{}_'.format(args['name']) if 'name' in args else ''

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    log_axis = args['log_axis'] if 'log_axis' in args else []
    title = args['title'] if 'title' in args else ''
    x = args['x'] if 'x' in args else list(range(len(y_list[0])))

    x_ticks = args['x_ticks'] if 'x_ticks' in args else None
    rotate = args['rotate'] if 'rotate' in args else False


    close = args['close'] if 'close' in args else 'all'
    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    for i, y in enumerate(y_list):
        simple_plot(save_dir, x=x, y=y, label=label_list[i], y_label=y_label, x_label=x_label, color= get_color(i+1),log_axis=log_axis, close=-1, ax=ax)

    ax.legend(fontsize=fontsize, frameon=True)
    ax.set_title(title, fontsize=fontsize)
    if rotate:
        plt.xticks(rotation=90)
    if x_ticks:
        ax.set_xticks(x_ticks['pos'])
        ax.set_xticklabels(x_ticks['label'])


    save_fig(f, os.path.join(save_dir, '{}_multiplot'.format(name)))

    if close != -1: plt.close(close)

    return ax

def simple_plot(y, **args):
    y_label = args['y_label'] if 'y_label' in args else 'y'
    x_label = args['x_label'] if 'x_label' in args else 'x'

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    y_lim = args['y_lim'] if 'y_lim' in args else None
    x_lim = args['x_lim'] if 'x_lim' in args else None


    log_axis = args['log_axis'] if 'log_axis' in args else []
    title = args['title'] if 'title' in args else ''


    close = args['close'] if 'close' in args else 'all'
    color = args['color'] if 'color' in args else 'black'
    marker = args['marker'] if 'marker' in args else '-'
    label = args['label'] if 'label' in args else None
    figsize = args['figsize'] if 'figsize' in args else (15, 10)

    x = args['x'] if 'x' in args else list(range(len(y)))

    x_tick_label = args['x_tick_label'] if 'x_tick_label' in args else None
    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=figsize)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    ax.grid(True)
    if label is not None:
        ax.plot(x, y, marker, color=color, label=label)
    else:
        ax.plot(x, y, marker, color=color)


    if x_lim:
        ax.set_xlim(x_lim)

    if y_lim is not None:
        ax.set_ylim(y_lim)

    ax.set_ylabel(y_label, fontsize=fontsize)
    ax.set_xlabel(x_label, fontsize=fontsize)
    if 'y' in log_axis: ax.set_yscale('log')
    if 'x' in log_axis: ax.set_xscale('log')

    ax.tick_params(axis='both', which='major', labelsize=fontsize)
    ax.set_title(title)

    if x_tick_label:
        ax.set_xticklabels(x_tick_label, fontsize=fontsize)

    if 'tight' in args: f.tight_layout()

    if close != -1: plt.close(close)

    return ax, f



def stem_plot(x, **args):

    y_label = args['y_label'] if 'y_label' in args else 'y'
    x_label = args['x_label'] if 'x_label' in args else 'x'

    fontsize = args['fontsize'] if 'fontsize' in args else 32
    y_lim = args['y_lim'] if 'y_lim' in args else None
    log_axis = args['log_axis'] if 'log_axis' in args else []
    title = args['title'] if 'title' in args else ''


    close = args['close'] if 'close' in args else 'all'
    color = args['color'] if 'color' in args else 'black'
    markerfmt = args['markerfmt'] if 'markerfmt' in args else None
    linefmt = args['linefmt'] if 'linefmt' in args else '-'
    basefmt = args['basefmt'] if 'basefmt' in args else ' '

    ref = args['ref'] if 'ref' in args else True
    label = args['label'] if 'label' in args else None
    x_lim = args['x_lim'] if 'x_lim' in args else None
    figsize = args['figsize'] if 'figsize' in args else (15, 10)
    markersize = args['markersize'] if 'markersize' in args else None


    y = args['y'] if 'y' in args else np.array([1.,] *len(x))

    x_tick_label = args['x_tick_label'] if 'x_tick_label' in args else None
    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=figsize)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']

    ax.grid(True)
    if label is not None:
        markerline, stemlines, baseline = ax.stem(x, y,  markerfmt=markerfmt,linefmt=linefmt, basefmt=basefmt,label=label, use_line_collection=True)
    else:
        markerline, stemlines, baseline  = ax.stem(x, y, markerfmt=markerfmt,linefmt=linefmt,  basefmt=basefmt,use_line_collection=True)


    if ref: ax.plot(x, np.full_like(x, -0.01), '|k', markeredgewidth=1)

    plt.setp(stemlines, 'color', color)
    plt.setp(markerline, 'color', color)
    if markersize: plt.setp(markerline, 'markersize', markersize)

    if x_lim:
        ax.set_xlim(x_lim)

    if y_lim is not None:
        ax.set_ylim(y_lim)



    ax.set_ylabel(y_label, fontsize=fontsize)
    ax.set_xlabel(x_label, fontsize=fontsize)
    if 'y' in log_axis: ax.set_yscale('log')
    if 'x' in log_axis: ax.set_xscale('log')

    ax.tick_params(axis='both', which='major', labelsize=fontsize)
    ax.set_title(title)

    if x_tick_label:
        ax.set_xticklabels(x_tick_label, fontsize=fontsize)

    if 'tight' in args: f.tight_layout()

    if close != -1: plt.close(close)

    return ax, f

def mean_var_plot(save_dir, x, name='', xlabel='x', ylabel='y', close='all'):
    n_samples, dim = x.shape
    mean = np.mean(x, axis=0)
    var = np.var(x, axis=0)
    x_range = list(range(dim))
    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    ax.plot(x_range, mean, 'o', label=r'$\mu$', color='black')

    # ax.legend(fontsize=32, frameon=True, ncol=2, handlelength=4, loc='center')
    ax.tick_params(axis='both', which='major', labelsize=20)
    ax.set_xlabel(xlabel, fontsize=32)
    ax.set_ylabel(r'$\mu$', fontsize=32)
    ax.grid(True)

    ax2 = ax.twinx()

    ax2.plot(x_range, var, '*', label=r'$\sigma^2$', color='green')
    ax2.set_ylabel(r'$\sigma^2$', fontsize=32)
    ax.tick_params(axis='both', which='major', labelsize=20)
    ax.legend(fontsize=32, frameon=True)

    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}mean_var'.format(name)))
    if close != -1: plt.close(close)


def var_plot(save_dir, x, name='', xlabel='x', close='all'):
    n_samples, dim = x.shape
    var = np.var(x, axis=0)
    x_range = list(range(dim))
    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)

    ax.plot(x_range, var, 'o', color='green')
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_xlabel(xlabel, fontsize=32)
    ax.set_ylabel(r'$\sigma^2$', fontsize=32)
    ax.grid(True)

    if name is not '':
        name = '{}_'.format(name)
    save_fig(f, os.path.join(save_dir, '{}var'.format(name)))
    if close != -1: plt.close(close)
