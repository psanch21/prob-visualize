from probvis.aux import save_fig
import matplotlib.pyplot as plt
import seaborn as sns
import os
def heatmap_plot(save_dir, matrix, **args):
    y_label = args['y_label'] if 'y_label' in args else 'y'
    y_ticks = args['y_ticks'] if 'y_ticks' in args else None
    x_label = args['x_label'] if 'x_label' in args else 'x'

    name = '{}_'.format(args['name'])if 'name' in args else ''
    fontsize = args['fontsize'] if 'fontsize' in args else 32
    close = args['close'] if 'close' in args else 'all'
    figsize = args['figsize'] if 'figsize' in args else (10, 10)


    f = plt.figure(figsize=figsize)
    ax = plt.subplot(1, 1, 1)
    sns.heatmap(matrix, ax=ax, vmin=0.0, vmax=1.0)
    ax.set_ylabel(y_label,  fontsize=fontsize)
    ax.set_xlabel(x_label, fontsize=fontsize)

    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_xticklabels([])
    if y_ticks is not None: ax.set_yticklabels(y_ticks)

    if 'tight' in args: f.tight_layout()

    save_fig(f, os.path.join(save_dir, '{}heatmap'.format(name)))
    if close != -1: plt.close(close)