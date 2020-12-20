import os

import matplotlib.pyplot as plt
import seaborn as sns
import probvis.aux as pva
import probvis.images as pvi

from probvis.aux import save_fig
from wordcloud import WordCloud
from probvis.aux import Cte
def plot_probs_with_images(images, probs, save_dir, name, close='all'):
    fig_list = list()
    n_samples = images.shape[0]

    h, w = images.shape[1:3]

    n_batches = int(n_samples / 8)
    for j in range(n_batches):
        f = plt.figure(figsize=Cte.FIGSIZE)
        i = 1
        k = 0
        for _ in range(8):
            idx = 8 * j + k
            ax = plt.subplot(8, 2, i)
            ax.plot(probs[idx, :])
            ax.set_title('Sample: {}'.format(idx))
            ax = plt.subplot(8, 2, i + 1)

            pvi.plot_image(images[idx], ax=ax)

            i += 2
            k += 1

        plt.subplots_adjust(hspace=0.2)
        f.savefig(os.path.join(save_dir, '{}_cat_p_i_{}.png'.format(name, j)))
        fig_list.append(f)
        if close != -1: plt.close(close)

    return fig_list


def plot_one_hot(one_hot, save_dir, name, close='all'):
    n_samples = one_hot.shape[0]

    one_hot = (one_hot == 1).tolist()

    one_hot = [one_hot[i].index(True) for i in range(n_samples)]

    f = plt.figure(figsize=Cte.FIGSIZE)
    ax = plt.subplot(1, 1, 1)
    sns.countplot(x=one_hot, ax=ax)

    f.savefig(os.path.join(save_dir, '{}_cat_count_onehot.png'.format(name)))

    if close != -1: plt.close(close)
    return f



def word_cloud_plot(save_dir, word_list, **args):
    words = ' '.join(word_list)
    name = '{}_'.format(args['name'])if 'name' in args else ''
    close = args['close'] if 'close' in args else 'all'
    colormap = args['colormap'] if 'colormap' in args else pva.get_random_cmap()
    relative_scaling =  args['relative_scaling'] if 'relative_scaling' in args else 0

    wordcloud = WordCloud(width=800, height=800,
                          background_color='black',
                          colormap=colormap,
                          relative_scaling=relative_scaling,
                          min_font_size=10).generate(words)

    f = plt.figure(figsize=(15, 15))
    ax = plt.subplot(1, 1, 1)

    ax.imshow(wordcloud, interpolation="bilinear")
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_aspect('equal')
    plt.axis('off')

    plt.subplots_adjust(wspace=0, hspace=0)
    if 'tight' in args: f.tight_layout()

    save_fig(f, os.path.join(save_dir, '{}image'.format(name)))
    if close != -1: plt.close(close)