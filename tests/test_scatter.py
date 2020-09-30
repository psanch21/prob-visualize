
import probvis.general.box as pvgb
import numpy as np
import probvis.aux as pva
pva.activate_latex_format()

#%%
save_dir = 'images'
n = 1000
x = list(range(n))
x1 = 10*np.random.random(n)
x2 = np.random.normal(0,1,n)

y1 = np.random.rand(n) + 0.1
y2 = np.random.normal(size=2*n)

y3 = np.random.exponential(100, 2*n) + 0.1
X = np.random.uniform(size=[n, 4])

# %%
f, ax = pvgb.box_plot(x_list=['a','b'], y_list=[y1, y2])
pva.save_fig(f, 'images/box_plot')


f, ax = pvgb.box_plot(x_list=['uni','expo'], y_list=[y1, y3], log=True)
pva.save_fig(f, 'images/box_plot_2_log')


f, ax = pvgb.box_plot(x_list=['uni','expo'], y_list=[y1, y3], log=True, showmeans={'color': 'black'})
pva.save_fig(f, 'images/box_plot_2_log_mean')



f, ax = pvgb.box_plot(x_list=['uni','expo'], y_list=[y1, y3])
pva.save_fig(f, 'images/box_plot_2')


f, ax = pvgb.box_plot(x_list=['uni','expo'], y_list=[y1, y3], showmeans={'color': 'darkblue', 'marker': 'D'})
pva.save_fig(f, 'images/box_plot_2_mean')



