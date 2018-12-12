import re

import numpy as np


def parse_line(line):
    regexp = r"""
    ^
    position=<\s*(-?\d+),\s*(-?\d+)\s*>\s*
    velocity=<\s*(-?\d+),\s*(-?\d+)\s*>
    $
    """
    x, y, vx, vy = map(int, re.match(regexp, line, re.VERBOSE).groups())
    return (x, y), (vx, vy)



def animate(frames):
    import matplotlib.pyplot as plt
    from IPython.display import HTML
    from matplotlib import animation
    # http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-as-interactive-javascript-widgets/
    # Does not work
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
        im.set_array(get_array(t))
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


def get_array(t, scale=1):
    points_t = points + t * velocities
    points_t = ((points_t - points_t.min(axis=0)) * scale).astype(np.int)
    xs, ys = points_t[:,0], points_t[:,1]
    xlim, ylim = (min(xs), max(xs)), (min(ys), max(ys))
    shape = xlim[1] - xlim[0] + 1, ylim[1] - ylim[0] + 1

    print(xlim, ylim)
    print(shape)

    array = np.zeros(shape)
    array[points_t[:,0], points_t[:,1]] = 1
    return array.T


def get_points(t):
    # they are upside-down and back-to-front but whatever
    points_t = points + t * velocities
    return points_t[:,0], points_t[:,1]


# path = "/tmp/10.txt"
path = "/Users/dan/tmp/aoc-2018/input/10.txt"
with open(path) as fp:
    points, velocities = map(np.array, zip(*map(parse_line, fp)))


def jupyter_notebook_cells():
    import matplotlib.pyplot as plt
    ######################
    nx, ny = 20, 2
    fig, axarr = plt.subplots(nx, ny, figsize=(20, 120))

    offset = 10700
    for i in range(nx):
        for j in range(ny):
            t = offset + i + j
            axarr[i, j].scatter(*get_points(t))
            axarr[i, j].set_title(f't = {t}')


    ######################

    fig = plt.figure(figsize=(12, 2))
    plt.scatter(*get_points(10710))

    #########################

    def dist(xs, ys):
        return np.sqrt((xs[1] - xs[0])**2 + (ys[1] - ys[0])**2)


    ts = range(10700, 10720)
    plt.scatter(ts, [dist(*get_points(t)) for t in ts])

    ##########################


def get_minimum_variance_generation(x, v):
    x_bar = x.mean(axis=0)
    v_bar = v.mean(axis=0)

    # centre the data at the origin
    x = x - x_bar

    t = -(x * (v - v_bar)).sum() / ((v - v_bar)**2).sum()

    return round(float(t))


def bitmap_array(points):
    points = points - points.min(axis=0)
    img = np.zeros(shape=points.max(axis=0) + 1, dtype='uint8')
    img[points[:,0], points[:,1]] = 1
    return img.T * 255


def get_message(points, velocities):
    from PIL import Image
    from pytesseract import image_to_string

    t = get_minimum_variance_generation(points, velocities)
    array = bitmap_array(points + t * velocities)
    img = Image.fromarray(array, mode="L")
    return image_to_string(img)  # DNW: returns empty string
