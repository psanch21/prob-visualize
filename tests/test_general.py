import probvis.general.general as pvg
import probvis.general.histogram as pvgh
import numpy as np
import probvis.aux as pva
from probvis.general.heatmap import heatmap_plot
pva.activate_latex_format()

save_dir = 'images/test'
n = 1000
x = list(range(n))
x1 = 10*np.random.random(n)
x2 = np.random.normal(0,1,n)

y1 = np.random.uniform(size=n)
y2 = np.random.random(size=n)

X = np.random.uniform(size=[n, 4])

#%%
# pvgh.hist_plot(save_dir=save_dir, x=x2, close=True, title='test')
# pvg.scater_plot_list(save_dir, x_list=[x1, x2], y_list=[y1, y2], color_list=['black', 'green'], label_list=['d1', 'd2'],
#                      name='test', alpha=1.0, xlabel=r'$\log_{10}$', ylabel=r'y', close='all')
#
# pvg.multi_hist_plot(save_dir, [x1, x2], [r'$||z||$', r'$||z_e||$'], name='ze', xlabel=r'Norm',
#                     density=False, alpha=0.7, fontsize=42)

# heatmap_plot(save_dir=save_dir, matrix=X.T, y_label=r'Category', x_label=r'Doc', tight=True)

pvg.multi_simple_plot(save_dir=save_dir, x=x, y_list=[y1, y2], label_list=['y1', 'y2'], log_axis=['x', 'y'])

#%%
import probvis.general.density_estimation as pvde

pvde.kde_plot(save_dir=save_dir, x=x1, bandwidth=0.01, xlabel=r'Events')