
import probvis.general.radar as pvgr
import numpy as np
import probvis.aux as pva
import matplotlib.pyplot as plt
pva.activate_latex_format()

save_dir = 'images'

x_list = np.random.random(4)
label_list = ['adgdgfd', 'bdfgd', 'cdfgdg', 'ddfgdhgdfgh']


# %%

f, ax = pvgr.radar_plot(y_list=x_list, label_list=label_list, color=pva.get_color(),
                        title='Radar Plot', fontsize_ticks={'y': 6, 'x': 12})

pva.save_fig(f, f'{save_dir}/radar_plot')


# %%

f, ax = plt.subplots(1, 6, subplot_kw=dict(polar=True), figsize=(15, 6))
for i in range(6):
    x_list = np.random.random(4)


    _, _ = pvgr.radar_plot(y_list=x_list, label_list=label_list, color=pva.get_color(),
                            title='Radar Plot', fontsize=12, ax=ax[i], fontsize_ticks={'y': 6, 'x': 12},
                           pad=20, y_lim=[0.0, 1.0])

f.tight_layout()

pva.save_fig(f, f'{save_dir}/radar_plot_multi')
plt.close('all')
