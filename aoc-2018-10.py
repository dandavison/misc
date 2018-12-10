import re

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib import animation


def parse_line(line):
    regexp = r"""
    ^
    position=<\s*(-?\d+),\s*(-?\d+)\s*>\s*
    velocity=<\s*(-?\d+),\s*(-?\d+)\s*>
    $
    """
    x, y, vx, vy = map(int, re.match(regexp, line, re.VERBOSE).groups())
    return (x, y), (vx, vy)


def animate(points, velocities, frames):
    points = points - points.min(axis=0)
    xs, ys = points[:,0], points[:,1]
    xlim, ylim = (min(xs), max(xs)), (min(ys), max(ys))
    shape = xlim[1] - xlim[0] + 1, ylim[1] - ylim[0] + 1

    dpi = 72.0
    xpx, ypx = shape
    figsize = ypx/dpi, xpx/dpi

    print(shape)
    print("figsize: ", figsize)

    fig = plt.figure(figsize=figsize, dpi=dpi)

    im = plt.figimage(np.zeros(shape))

    def init():
        return (im,)

    def get_frame(t):
        points_t = points + t * velocities
        array = np.zeros(shape)
        # print(array.shape)
        # print(points_t)
        array[points_t[:,0], points_t[:,1]] = 1
        im.set_array(array)
        return (im,)

    anim = animation.FuncAnimation(
        fig,
        get_frame,
        init_func=init,
        frames=frames,
        interval=20,
        blit=True,
    )

    return HTML(anim.to_html5_video())


path = "/tmp/10.txt"
# path = "/Users/dan/tmp/aoc-2018/input/10.txt"
with open(path) as fp:
    points, velocities = map(np.array, zip(*map(parse_line, fp)))

animate(points, velocities, frames=1000)
