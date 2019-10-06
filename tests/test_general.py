import probvis.general as pvg
import numpy as np
import probvis.aux as pva

pva.activate_latex_format()

save_dir = 'images'
n = 100
x1 = 10*np.random.random(n)
x2 = np.random.normal(0,1,n)

y1 = np.random.uniform(size=n)
y2 = np.random.random(size=n)
pvg.scater_plot_list(save_dir, x_list=[x1, x2], y_list=[y1, y2], color_list=['black', 'green'], label_list=['d1', 'd2'],
                     name='test', alpha=1.0, xlabel=r'$\log_{10}$', ylabel=r'y', close='all')
