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


def threshold_image(image, threshold):
    new_image = image.copy()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            new_image[i, j] = 0 if image[i, j] < threshold else 255

    return new_image
