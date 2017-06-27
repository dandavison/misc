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
    Return highest density interval with proportion p_area of area.

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


class TestHighestDensityInterval(unittest.TestCase):

    def test_isosceles_triangle(self):
        """
        Test interval calculation under a symmetric triangle.

        The triangle has bottom left corner at (0, 0), and bottom right corner
        at (0, base).
        """
        theta = np.pi / 5  # gradient and -gradient of the two line segments
                           # forming the sides of the triangle
        base = 1           # length of line segment forming base of triangle
        p_area = 0.95      # desired proportion of area

        def f(x):
            """
            A function describing two sides of an isosceles triangle.

            The third side of the triangle is the segment [0, base] of the x
            axis.
            """
            assert 0 <= x <= base
            if x < base / 2:
                return x * np.tan(theta)
            else:
                return (base - x) * np.tan(theta)

        area = (base ** 2) * np.tan(theta) / 4  # absolute area of triangle
        area_outside_interval = area * (1 - p_area)

        # Consider the right-triangle T, which lies outside the highest density
        # interval, to the left. The bottom-left corner of T is at the origin.
        # Therefore the adjacent of T is the expected left bound for the
        # returned interval.
        # Solve for the adjacent:
        expected_left_bound = np.sqrt(area_outside_interval / np.tan(theta))
        expected_right_bound = base - expected_left_bound

        x = np.linspace(0, base, 1e4)
        y = np.array(map(f, x))
        left, right = highest_density_interval(x, y, p_area)

        self.assertAlmostEqual(left, expected_left_bound)
        self.assertAlmostEqual(right, expected_right_bound)

    def test_gaussian(self):
        "Test interval calculation under a symmetric curve."
        mean = 100
        sd = 20
        dist = stats.norm(mean, sd)
        p_area = 0.95
        tail_prob = (1 - p_area) / 2

        expected_left_bound = dist.ppf(tail_prob)
        expected_right_bound = dist.ppf(1 - tail_prob)

        x = np.linspace(-200, 400, 1e6)
        y = dist.pdf(x)
        tol = 1e-7
        left, right = highest_density_interval(x, y, p_area)

        self.assertAlmostEqual(left, expected_left_bound)
        self.assertAlmostEqual(right, expected_right_bound)

    def test_gamma(self):
        "Test interval calculation under an asymmetric curve."
        if True:
            return
        shape, loc, scale = 2, 0, 1
        dist = stats.gamma(shape, loc=loc, scale=scale)
        p_area = 0.95
        tail_prob = (1 - p_area) / 2

        expected_left_bound = dist.ppf(tail_prob)
        expected_right_bound = dist.ppf(1 - tail_prob)

        x = np.linspace(0, 40, 1e6)
        y = dist.pdf(x)
        tol = 1e-7
        left, right = highest_density_interval(x, y, p_area, xtol=1e-6, ftol=1e-6)

        self.assertAlmostEqual(left, expected_left_bound)
        self.assertAlmostEqual(right, expected_right_bound)

    def assertAlmostEqual(self, a, b):
        eps = 1e-8
        self.assertTrue(abs(a - b) < eps)


if __name__ == '__main__':
    unittest.main()
