
import numpy as np
def exponential_kernel(u, alpha, beta):

    return alpha * beta* np.exp(-beta*u)

def powerlaw_kernel(u, alpha, beta, p):
    num = alpha*beta
    den = np.power((1 + beta*u ), p)
    return np.divide(num, den)