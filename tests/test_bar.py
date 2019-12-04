import probvis.general as pvg
import numpy as np
import probvis.aux as pva
from probvis.general.bar import bar_plot
pva.activate_latex_format()

save_dir = 'images'
n = 100
x1 = 10*np.random.random(n)

y1 = np.random.uniform(size=n)

bar_plot(save_dir=save_dir, x=x1 ,y=y1, y_label=r'$N_u$', x_label=r'User $u$', name='tweets_per_user', tight=True, close=True,  fontsize=16, ticksize=6)