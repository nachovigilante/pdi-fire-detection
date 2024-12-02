from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
from PIL import Image


def load_image(image_path):
    image = Image.open(image_path)
    return np.array(image)


def show_image(image):
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image)


def show_images(images, titles=None):
    _, axes = plt.subplots(1, len(images), figsize=(20, 10))
    for i, (image, ax) in enumerate(zip(images, axes)):
        ax.set_xticks([])
        ax.set_yticks([])
        ax.imshow(image, cmap=cm.gray, vmin=0, vmax=255)
        if titles is not None:
            ax.set_title(titles[i])
    plt.show()


def show_histogram(histogram_values):
    plt.figure(figsize=(20, 10))
    plt.bar(range(256), histogram_values)
    plt.show()


def show_histograms(histogram_values, titles=None):
    _, axes = plt.subplots(len(histogram_values), 1, figsize=(20, 10))
    for i, (histogram, ax) in enumerate(zip(histogram_values, axes)):
        ax.bar(range(256), histogram)
        if titles is not None:
            ax.set_title(titles[i])
    plt.show()


def binarizar(imag, thres, index):
    h, w, _ = imag.shape
    img_res = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            if imag[i, j, index] >= thres:
                img_res[i, j] = 1
    return img_res


def statistical_ciel(img_lab):
    # h, w, _ = img_lab.shape
    # n = h * w
    # ln = 0
    # an = 0
    # bn = 0
    # for i in range(h):
    #    for j in range(w):
    #        ln += img_lab[i, j, 0]
    #        an += img_lab[i, j, 1]
    #        bn += img_lab[i, j, 2]
    #
    # ln = ln / n
    # an = an / n
    # bn = bn / n
    #
    # return (ln, an, bn)
    # o devolver
    return (
        np.mean(img_lab[:, :, 0]),
        np.mean(img_lab[:, :, 1]),
        np.mean(img_lab[:, :, 2]),
    )
    # o quizás funciona
    # return np.mean(img, axis=2)
