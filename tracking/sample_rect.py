import os
from PIL import Image
import matplotlib.pyplot as plt

def draw_rect(image,rects,dir,i):
    dpi = 80.0
    figsize = (image.size[0] / dpi, image.size[1] / dpi)

    fig = plt.figure(frameon=False, figsize=figsize, dpi=dpi)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    im = ax.imshow(image, aspect='auto')

    for r in rects:
        this_rect = plt.Rectangle(tuple(r[:2]), r[2], r[3],
                                    linewidth=3, edgecolor="#ffff00", zorder=1, fill=False)
        ax.add_patch(this_rect)
    plt.pause(.01)
    plt.draw()
    fig.savefig(os.path.join('results/Tiger1/sams', '{:04d}.jpg'.format(i)), dpi=dpi)
