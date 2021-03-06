import matplotlib

import numpy as np

matplotlib.use('PS')
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import random

import shutil

try:
    from tikzplotlib import save as tikz_save
except Exception as exc:
    print(exc)

# %% Contants
CMAPS = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
         'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
         'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

#  list(mcolors.CSS4_COLORS.keys())

MARKERS = ['o', 'D', 'x', 'v', 's', '^']
LINESTYLES = ['solid',
              (0, (5, 10)), # Loosely dashed
              (0, (3, 5, 1, 5, 1, 5)), # 'dashdotdotted',
              (0, (3, 10, 1, 10, 1, 10)), #'loosely dashdotdotted',
              (0, (3, 10, 1, 10)), #'loosely dashdot',
              'dashed', 'dotted', 'dashdot']

COLORS = ['#1f77b4',
          '#ff7f0e',
          '#2ca02c',
          '#d62728',
          '#9467bd',
          '#8c564b',
          '#e377c2',
          '#7f7f7f',
          '#bcbd22',
          '#17becf']


# COLORS = ['blue', 'orange', 'green', 'red', 'grey', 'purple', 'lime', 'indigo', 'orange', 'black']
COLORS_FULL = ['darkblue',
               'darkgreen',
               'darkred',
               'goldenrod',
               'darkcyan',
               'darkviolet',
               'goldenrod',
               'black',
               'darkorange',
               'purple',
               'steelblue',
               'lightpink',
               'lavenderblush',
               'gold',
               'powderblue',
               'paleturquoise',
               'burlywood',
               'lightgrey',
               'cornflowerblue',
               'greenyellow',
               'cornsilk',
               'palevioletred',
               'olive',
               'dimgray',
               'bisque',
               'lavender',
               'lightyellow',
               'gray',
               'lightgreen',
               'slateblue',
               'forestgreen',
               'tomato',
               'maroon',
               'lightcoral',
               'beige',
               'salmon',
               'crimson',
               'mediumspringgreen',
               'lightslategray',
               'lightgoldenrodyellow',
               'lightskyblue',
               'mediumseagreen',
               'orangered',
               'blanchedalmond',
               'lightsalmon',
               'rebeccapurple',
               'dodgerblue',
               'palegoldenrod',
               'yellowgreen',
               'snow',
               'cadetblue',
               'violet',
               'mediumpurple',
               'darkgrey',
               'blueviolet',
               'yellow',
               'deeppink',
               'mediumvioletred',
               'azure',
               'aliceblue',
               'darkmagenta',
               'cyan',
               'fuchsia',
               'sienna',
               'lightslategrey',
               'lightsteelblue',
               'whitesmoke',
               'floralwhite',
               'mediumaquamarine',
               'antiquewhite',
               'springgreen',
               'mediumblue',
               'mistyrose',
               'slategray',
               'lawngreen',
               'white',
               'orange',
               'royalblue',
               'navy',
               'ghostwhite',
               'papayawhip',
               'slategrey',
               'darkkhaki',
               'darksalmon',
               'darkgoldenrod',
               'indianred',
               'skyblue',
               'oldlace',
               'blue',
               'plum',
               'mediumorchid',
               'indigo',
               'pink',
               'thistle',
               'darkseagreen',
               'deepskyblue',
               'firebrick',
               'darkolivegreen',
               'olivedrab',
               'green',
               'peru',
               'mediumturquoise',
               'silver',
               'darkgray',
               'seashell',
               'lightgray',
               'saddlebrown',
               'lightcyan',
               'tan',
               'darkslategrey',
               'darkorchid',
               'chartreuse',
               'coral',
               'peachpuff',
               'magenta',
               'lightseagreen',
               'orchid',
               'khaki',
               'chocolate',
               'wheat',
               'mintcream',
               'aqua',
               'limegreen',
               'honeydew',
               'ivory',
               'turquoise',
               'sandybrown',
               'brown',
               'gainsboro',
               'darkslategray',
               'dimgrey',
               'moccasin',
               'hotpink',
               'palegreen',
               'teal',
               'red',
               'darkslateblue',
               'midnightblue',
               'navajowhite',
               'mediumslateblue',
               'lime',
               'lemonchiffon',
               'grey',
               'darkturquoise',
               'linen',
               'rosybrown',
               'seagreen',
               'lightblue',
               'aquamarine']
# %%
IS_LATEX = False
IS_PDF = True


class Cte:
    FIGSIZE=(4,3)
# %%


def get_random_cmap():
    return random.choice(CMAPS)


def get_color(id=-1):
    n = len(COLORS)
    if id < 0 or id >= n:
        return random.choice(COLORS)
    else:
        return COLORS[id]


def get_marker(id=-1):
    n = len(MARKERS)
    if id < 0 or id >= n:
        return random.choice(MARKERS)
    else:
        return MARKERS[id]


def get_linestyle(id=-1):
    n = len(LINESTYLES)
    if id < 0 or id >= n:
        return random.choice(LINESTYLES)
    else:
        return LINESTYLES[id]


def get_color_list(id_list):
    if isinstance(id_list, int):
        return [get_color(i) for i in range(id_list)]
    elif isinstance(id_list, list):
        return [get_color(i) for i in id_list]


def activate_pdf_format(value):
    global IS_PDF
    IS_PDF = value

    return


def activate_latex_format():
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')


# %%

def save_fig(f, complete_fig_name, dpi=240, bbox_inches='tight'):
    print('Fig name: {}'.format(complete_fig_name))
    if IS_PDF:
        f.savefig('{}.pdf'.format(complete_fig_name), dpi=dpi, bbox_inches=bbox_inches)
    else:
        f.savefig('{}.png'.format(complete_fig_name), dpi=dpi, bbox_inches=bbox_inches)
    if IS_LATEX:
        try:
            tikz_save('{}.tex'.format(complete_fig_name), encoding='utf8')
        except NameError:
            print('NameError in tikz_save')


def create_dir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    return folder


def clear_dir(folder):
    try:
        shutil.rmtree(folder)
    except:
        pass

    return create_dir(folder)


def remove(filename):
    if os.path.exists(filename):
        os.remove(filename)
    return


# %% Axis

def set_x_axis_style(ax, labels, label=None):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    if label: ax.set_xlabel(label)



def export_legend(legend, filename):
    fig = legend.figure
    fig.canvas.draw()
    bbox = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    filename+='.png'
    fig.savefig(filename, dpi="figure", bbox_inches=bbox)
