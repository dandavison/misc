import matplotlib

matplotlib.use("Qt5Agg")

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np


plt.close()

xx = range(10)
yy = [i / 10 for i in xx]


# This plots ten circles all with the same color
plt.plot(xx, yy, "o")

# Now, how do we make their color be determined by their y value?

plt.close()

colors = cm.Reds(yy)

for x, y, col in zip(xx, yy, colormap):
    plt.plot(x, y, "o", color=col)
