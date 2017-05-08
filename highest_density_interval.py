from scipy import integrate
from scipy import interpolate
from scipy import optimize


def highest_density_interval(x, y, credible_mass=0.95):
    """
    Return highest density interval with probability mass p.

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
        if 0 <= p <= 1 - credible_mass:
            return inv_cdf(p + credible_mass) - inv_cdf(p)
        else:
            return np.inf

    p = optimize.fmin(
        interval_width,
        x0=0,
        disp=False,
    )[0]

    return inv_cdf([p, min(p + credible_mass, 1)])
