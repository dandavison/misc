"""
A point on the surface of a sphere is specified using 2 coordinates:
- longitude (0, 2\pi)
- latitude
"""
from math import pi




def random_triangle():
    u = uniform(0, 2*pi, 3)
    p1 = (0, 0)
    p2 = (0, u[0])
    p3 = (u[1], u[2])
    return (p1, p2, p3)


def contains(triangle, point):


if __name__ == '__main__':

    for i in range(N):
        triangle = generate_random_triangle()
        if contains_point(triangle):
            n_inside += 1

    print(n)

    print(estimate_average_triangular_surface_proportion(N=1000))
