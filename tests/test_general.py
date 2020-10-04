import probvis.general.general as pvg
import probvis.general.histogram as pvgh
import numpy as np
import probvis.aux as pva
import os
import matplotlib.pyplot as plt

pva.activate_latex_format()

save_dir = 'images'
n = 1000
x = list(range(n))
x1 = 10 * np.random.random(n)
x2 = np.random.normal(0, 1, n)

y1 = np.random.uniform(size=n)
y2 = np.random.random(size=n)
y3 = np.random.normal(size=n)

loc = np.array([0, 2, 5, 10]).repeat(3).reshape(4, 3).T
X = np.random.normal(loc=loc, scale=1)

# %%
# pvgh.hist_plot(save_dir=save_dir, x=x2, close=True, title='test')
# pvg.scater_plot_list(save_dir, x_list=[x1, x2], y_list=[y1, y2], color_list=['black', 'green'], label_list=['d1', 'd2'],
#                      name='test', alpha=1.0, xlabel=r'$\log_{10}$', ylabel=r'y', close='all')
#
# pvg.multi_hist_plot(save_dir, [x1, x2], [r'$||z||$', r'$||z_e||$'], name='ze', xlabel=r'Norm',
#                     density=False, alpha=0.7, fontsize=42)

# heatmap_plot(save_dir=save_dir, matrix=X.T, y_label=r'Category', x_label=r'Doc', tight=True)

# pvg.multi_simple_plot(save_dir=save_dir, x=x, y_list=[y1, y2], label_list=['y1', 'y2'], log_axis=['x', 'y'], x_tick_label=[1,4,5,6])
pvg.multi_simple_plot(save_dir=save_dir, x=x, y_list=[y1, y2], label_list=['y1', 'y2'],
                      x_ticks={'pos': [990.5, 100], 'label': ['a', 'b']}, rotate=True)

# %%

f = plt.figure(figsize=(30, 10))
ax = plt.subplot(1, 1, 1)

ax, _ = pvg.stem_plot(x=x2[::20], markerfmt='D', linefmt='-', color='red', ax=ax)
ax, _ = pvg.stem_plot(x=x1[::20], markerfmt='o', linefmt='-', color='blue', ax=ax)
pva.save_fig(f, os.path.join(save_dir, 'stem'))

# %%
import probvis.general.density_estimation as pvde

pvde.kde_plot(x=x1, bandwidth=0.01, x_label=r'\textbf{Bold} $\log \mu$', pad=20)

plt.show()

# %% Test Violin

import probvis.general.violin as pvv

pvv.violin_plot(save_dir=save_dir, data_list=[y1, y2, x2], label_list=['n1', r'$\epsilon$', r'gauss'],
                showmeans=True,
                quartiles=[25, 75],
                color_list=[pva.get_color(1), pva.get_color(2), pva.get_color(3)],
                ylabel='ESS')

# %% Heatmap

import probvis.general.heatmap as pvghm

f, ax = pvghm.heatmap_plot_cols(matrix=X,
                                tight=True, annot=True, fmt='.2f',
                                figsize=(20, 8),
                                y_ticks=['ejjjvgvg', 'e', 'h'],
                                x_ticks=['aaaaa', 'bbb', 'cccc', 'ddddd'],
                                rotation_x=-45,
                                cbar=True)

pva.save_fig(f, 'images/heatmap')

# %%
from matplotlib.ticker import FixedFormatter

f = plt.figure(figsize=(15, 10))
ax = plt.subplot(1, 1, 1)

b = np.argsort(np.argsort(X, axis=0), axis=0)

im = ax.imshow(b, aspect="auto", cmap="coolwarm")
f.colorbar(im, ax=ax, ticks=np.array([0.0, 0.5, 1.0]) * b.max(),
           format=FixedFormatter(["low", "middle", "high"]))

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        ax.text(j, i, X[i, j], ha="center", va="center")
pva.save_fig(f, 'images/heatmap_2')
plt.close('all')
