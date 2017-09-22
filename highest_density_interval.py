from __future__ import division
from __future__ import print_function

import unittest

import numpy as np
from scipy import integrate
from scipy import interpolate
from scipy import optimize
from scipy import stats


def highest_density_interval(x, y, p_area=0.95, **kwargs):
    """
    Return the highest density interval with proportion p_area of area.

    The highest density intervals is, out of all intervals with proportion
    p_area of area, the interval over which the average value of the function
    is maximized.

    x and y are 1-dimensional arrays of the same length, specifying the value
    of the function y at grid points x. I.e. y[i] = f(x[i]), where f is the
    function for which a highest density interval is desired. f will typically
    represent a probability distribution, but it need not be
    normalized (i.e. it need not integrate to 1). So f could represent a
    likelihood function, or the product of a likelihood function and a prior
    function.

    Based on hdi.function https://CRAN.R-project.org/package=HDInterval
    """
    assert len(x) == len(y)
    s = integrate.cumtrapz(y, x, initial=0)
    cdf = s / s[-1]  # normalize the integral to total area 1
    inv_cdf = interpolate.interp1d(cdf, x)

    def interval_width(p):
        if 0 <= p <= 1 - p_area:
            return inv_cdf(p + p_area) - inv_cdf(p)
        else:
            return np.inf

    p = optimize.fmin(
        interval_width,
        x0=0,
        disp=False,
        **kwargs
    )[0]

    return inv_cdf([p, min(p + p_area, 1)])




if __name__ == '__main__':
    unittest.main()
