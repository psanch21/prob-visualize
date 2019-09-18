import os

import matplotlib.pyplot as plt
import seaborn as sns


def plot_one_hot(one_hot, save_dir, name, close=None):
    n_samples = one_hot.shape[0]

    one_hot = (one_hot == 1).tolist()

    one_hot = [one_hot[i].index(True) for i in range(n_samples)]

    f = plt.figure(figsize=(15, 10))
    ax = plt.subplot(1, 1, 1)
    sns.countplot(x=one_hot, ax=ax)

    f.savefig(os.path.join(save_dir, '{}_cat_count_onehot.png'.format(name)))

    if close != -1: plt.close(close)
    return f
