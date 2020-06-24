# %%
# import probvis.general as pvg
import numpy as np
import probvis.aux as pva
from probvis.general.bar import bar_plot
pva.activate_latex_format()

save_dir = 'images'
n = 100
x1 = [ str(i) for i in 10*np.random.random(n)]

y1 = np.random.uniform(size=n)
# %%
ax, f = bar_plot( y=x1 ,x=y1, y_label=r'$N_u$', x_label=r'User $u$', tight=True,
                  fontsize=16, ticksize=6, rotation=90, orient='h')

pva.save_fig(f, 'images/bar')