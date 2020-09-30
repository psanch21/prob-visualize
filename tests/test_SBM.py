
# %%
import probvis.general.box as pvgb
import numpy as np
import probvis.aux as pva
import pandas as pd
pva.activate_latex_format()
import random
import matplotlib.pyplot as plt
import seaborn as sns



model_list = ['model1', 'model2', 'model3']
dataset_list = ['data1', 'data2', 'data3']

# %%
df = pd.DataFrame(columns=['model', 'dataset', 'F1 score', 'NMI'])

for i in range(100):
    idx_model, idx_data = np.random.randint(3), np.random.randint(3)

    F1 = np.random.uniform(0, idx_data+1)
    NMI = np.random.uniform(1, idx_model+2)

    df.loc[len(df)] = [model_list[idx_model], dataset_list[idx_data],F1, NMI]



# %%

f, ax = pvgb.box_plot_from_df(df=df, x='dataset',y='NMI', hue='model', y_label='MuMI',
                              grid=False)
pva.save_fig(f, 'images/box_plot_from_df')

