def subplot_different_sizes_pyplot():
    list1 = [1, 2, 3, 4]
    ax = plt.subplot(3, 1, (1, 2))
    ax.plot(list1)
    ax = plt.subplot(3, 1, 3)


def subplot_different_sizes_oo():
    list1 = [1, 2, 3, 4]
    fig = plt.figure()
    ax = fig.add_subplot(3, 1, (1, 2))
    ax.plot(list1)
    ax = fig.add_subplot(3, 1, 3)
