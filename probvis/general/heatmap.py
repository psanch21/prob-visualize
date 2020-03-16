from probvis.aux import save_fig
import matplotlib.pyplot as plt
import seaborn as sns
import os
def heatmap_plot(save_dir, matrix, **args):
    y_label = args['y_label'] if 'y_label' in args else 'y'
    y_ticks = args['y_ticks'] if 'y_ticks' in args else None
    x_ticks = args['x_ticks'] if 'x_ticks' in args else None
    x_label = args['x_label'] if 'x_label' in args else 'x'

    name = '{}_'.format(args['name'])if 'name' in args else ''
    fontsize = args['fontsize'] if 'fontsize' in args else 32
    close = args['close'] if 'close' in args else 'all'
    title = args['title'] if 'title' in args else ''
    figsize = args['figsize'] if 'figsize' in args else (15, 10)

    vmin = args['vmin'] if 'vmin' in args else 0.0
    vmax = args['vmax'] if 'vmax' in args else 1.0

    f = None
    if 'ax' not in args:
        f = plt.figure(figsize=figsize)
        ax = plt.subplot(1, 1, 1)
    else:
        ax = args['ax']
    sns.heatmap(matrix, ax=ax, vmin=vmin, vmax=vmax)
    ax.set_ylabel(y_label,  fontsize=fontsize)
    ax.set_xlabel(x_label, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)

    ax.tick_params(axis='both', which='major', labelsize=16)
    if x_ticks is None: ax.set_xticklabels([])
    if y_ticks is not None: ax.set_yticklabels(y_ticks)

    if 'tight' in args: f.tight_layout()

    if f is not None: save_fig(f, os.path.join(save_dir, '{}heatmap'.format(name)))
    if close != -1: plt.close(close)
