import matplotlib
# matplotlib.use('TkAgg')
# matplotlib.use('Agg')
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_gamma(shape=1, loc=1, scale=1, x_range=(0, 20), n_grid=100):
    gamma = stats.gamma(shape, loc=loc, scale=scale)
    x = np.linspace(*x_range, num=n_grid)
    plt.plot(x, gamma.pdf(x))
    # plt.savefig('/vagrant/z.png')
    plt.show()

plot_gamma()
