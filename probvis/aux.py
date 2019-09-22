import matplotlib
matplotlib.use('PS')
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import random
import seaborn as sns

try:
    from tikzplotlib import save as tikz_save
except Exception as exc:
    print(exc)


#%%
IS_LATEX = True

#%%

def save_fig(f, complete_fig_name):
    print('Fig name: {}'.format(complete_fig_name))
    f.savefig(complete_fig_name + '.png')
    if IS_LATEX:
        try:
            tikz_save(complete_fig_name + '.tex')
        except NameError:
            print('NameError in tikz_save')
