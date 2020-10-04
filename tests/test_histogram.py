
import probvis.general.general as pvg
import probvis.general.histogram as pvgh
import numpy as np
import probvis.aux as pva
pva.activate_latex_format()

#%%
save_dir = 'images'
n = 1000
x = list(range(n))
x1 = 10*np.random.random(n)
x2 = np.random.normal(0,1,n)

y1 = np.random.rand(n)
y2 = np.random.random(size=n)

X = np.random.uniform(size=[n, 4])

# %%
pvgh.multi_hist_plot(save_dir=save_dir,
                     data_list=[x1 for i in range(3)],
                     label_list=[str(i) for i in range(3)] ,
                     name='a', color_list=None, xlabel='derivate', ylabel='$\mathrm{E}_e[I_{es}^f]$', density=True,
                    logy=False, alpha=0.7, fontsize=32, close=-1, binwidth=0.01, x_lim=None, v_line=0.5)



# %%
f, ax = pvgh.hist_plot(x=y1, density=True, histtype='stepfilled', alpha=0.1, linewidth=4)

pva.save_fig(f, 'images/hist_test')

# %%

f, ax = pvgh.hist_plot(x=y1, xlabel='derivate', ylabel='prob',
                    logx=True, bins=10, alpha=0.7)

pva.save_fig(f, 'images/hist_test_logx')


f, ax = pvgh.hist_plot(x=y1, xlabel='derivate', ylabel='prob',
                    logx=True, density=True, bins=10, alpha=0.7)

pva.save_fig(f, 'images/hist_test_logx_density')


