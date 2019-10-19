from probvis.aux import save_fig
import matplotlib.pyplot as plt
import seaborn as sns
import os
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