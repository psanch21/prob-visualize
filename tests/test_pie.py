
import probvis.general.pie as pvgp
import numpy as np
import probvis.aux as pva
import matplotlib.pyplot as plt
pva.activate_latex_format()

#%%
save_dir = 'images'

size_list = np.random.dirichlet([1,]*4)
label_list = ['adgdgfd', 'bdfgd', 'cdfgdg', 'ddfgdhgdfgh']


# %%

f, ax = pvgp.pie_plot(size_list=size_list, label_list=label_list)

pva.save_fig(f, f'{save_dir}/pie_plot')

f, ax = pvgp.pie_plot(size_list=size_list, label_list=label_list, color_list=pva.get_color_list([10,2,3,4]), explode=0.02, fontsize=48, tight=True)

pva.save_fig(f, f'{save_dir}/pie_plot_explode')

