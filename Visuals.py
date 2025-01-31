import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection



def plot_image(image, title=""):
    plt.figure()
    plt.title(title)
    plt.imshow(image)
    plt.show()


def plot_grid(x,y, ax=None, **kwargs):
    ax = ax or plt.gca()
    segs1 = np.stack((x,y), axis=2)
    segs2 = segs1.transpose(1,0,2)
    kwargs.setdefault('linewidth', 0.5)
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))

    ax.autoscale()
    # Make lines smaller

