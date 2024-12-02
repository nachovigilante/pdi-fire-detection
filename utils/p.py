import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import cm


def ps(vec_imgs, vec_masks):
    # histogramas
    p_ab = np.zeros((24, 24))
    p_la = np.zeros((24, 24))
    p_lb = np.zeros((24, 24))
    cant = len(vec_imgs)
    pxs = 0

    for k in range(0, cant):
        img = vec_imgs[k]
        mask = vec_masks[k]
        h, w, _ = img.shape
        for i in range(h):
            for j in range(w):
                if mask[i, j]:
                    # aumentar en 1 la,lb,ab
                    l = img[i, j, 0]
                    a = img[i, j, 1]
                    b = img[i, j, 2]
                    l_ind = math.floor(24 * l / 101)
                    a_ind = math.floor(24 * (a + 110) / 221)
                    b_ind = math.floor(24 * (b + 110) / 221)
                    p_la[l_ind, a_ind] += 1
                    p_lb[l_ind, b_ind] += 1
                    p_ab[a_ind, b_ind] += 1
                    pxs += 1

    p_la = p_la / pxs
    p_lb = p_lb / pxs
    p_ab = p_ab / pxs

    return (p_la, p_lb, p_ab)


def p_lab(l, a, b, p1, p2, p3):
    l_ind = math.floor(24 * l / 101)
    a_ind = math.floor(24 * (a + 110) / 221)
    b_ind = math.floor(24 * (b + 110) / 221)
    return p1[l_ind, a_ind] * p2[l_ind, b_ind] * p3[a_ind, b_ind]


def print_ps(p1, p2, p3):
    # documentación matplotlib
    fig, ax = plt.subplots(1, 3, subplot_kw={"projection": "3d"}, figsize=(10, 10))
    # fig, axes = plt.subplots(2, 4, figsize=(15, 8))

    # Make data.
    X = np.arange(0, 24, 1)
    Y = np.arange(0, 24, 1)
    X, Y = np.meshgrid(X, Y)
    R = (X, Y)
    Z1 = p1[R]
    Z2 = p2[R]
    Z3 = p3[R]

    # Plot the surface.
    surf1 = ax[0].plot_surface(
        Y, X, Z1, cmap=cm.coolwarm, linewidth=0, antialiased=False
    )

    surf2 = ax[1].plot_surface(
        X, Y, Z2, cmap=cm.coolwarm, linewidth=0, antialiased=False
    )

    surf3 = ax[2].plot_surface(
        X, Y, Z3, cmap=cm.coolwarm, linewidth=0, antialiased=False
    )

    ax[0].set_xlabel("a")
    ax[0].set_ylabel("l")
    ax[0].invert_xaxis()
    ax[0].invert_yaxis()

    ax[1].set_xlabel("L")
    ax[1].set_ylabel("b")
    ax[1].invert_yaxis()

    ax[2].set_xlabel("a")
    ax[2].set_ylabel("b")
    ax[2].invert_yaxis()
    # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
