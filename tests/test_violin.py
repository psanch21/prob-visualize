
import probvis.general.violin as pvgv
import numpy as np
import probvis.aux as pva
pva.activate_latex_format()

#%%
save_dir = 'images'
n = 1000
x = list(range(n))
x1 = 10*np.random.random(n)
x2 = np.random.normal(0,1,n)

y1 = np.random.rand(n) + 0.001
y2 = np.random.normal(size=2*n)

y3 = np.random.exponential(10, 2*n) + 0.001
X = np.random.uniform(size=[n, 4])

# %%



f, ax = pvgv.violin_plot(x_list=['uni','expo'], y_list=[y1, y3], showmeans={'color': 'darkblue', 'marker': 'D'},
                      color_list=[pva.get_color(1), pva.get_color(2)],
                      y_label='ESS',
                         log=False,
                      )

pva.save_fig(f, 'images/violin')


f, ax = pvgv.violin_plot(x_list=['uni','expo'], y_list=[y1, y3], showmeans={'color': 'darkblue', 'marker': 'D'},
                      color_list=[pva.get_color(1), pva.get_color(3)],
                      y_label='ESS',
                         log=True,
                      )

pva.save_fig(f, 'images/violin_log')
