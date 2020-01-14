import os

import probvis.general.general as pvg

import numpy as np

def plot_pdf(save_dir, **args):
    n_samples = args['n'] if 'n' in args else 1000
    mu = args['mean'] if 'mean' in args else 3
    sigma = args['sigma'] if 'sigma' in args else 1


    s = np.random.lognormal(mu, sigma, n_samples)
    x = np.linspace(np.min(s),np.max(s),n_samples)
    pdf = (np.exp(-(np.log(x) - mu) ** 2 / (2 * sigma ** 2))/ (x * sigma * np.sqrt(2 * np.pi)))

    name = 'ln_{}_{}'.format(mu, sigma)

    pvg.simple_plot(save_dir=save_dir, y=pdf, x=x, name=name, title=r'LN(x)', x_label=r'x', y_label=r'p(x)', tight=True)

