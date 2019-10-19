import matplotlib

matplotlib.use('PS')
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os

try:
    from tikzplotlib import save as tikz_save
except Exception as exc:
    print(exc)

# %%
IS_LATEX = False


def activate_latex_format():
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')


# %%

def save_fig(f, complete_fig_name):
    print('Fig name: {}'.format(complete_fig_name))
    f.savefig('{}.pdf'.format(complete_fig_name), dpi=300)
    if IS_LATEX:
        try:
            tikz_save('{}.tex'.format(complete_fig_name), encoding='utf8')
        except NameError:
            print('NameError in tikz_save')


def create_dir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    return folder
