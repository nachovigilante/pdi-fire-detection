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

def binarizar(imag, thres, index):
    h, w, _ = imag.shape
    img_res = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            if imag[i, j, index] >= thres:
                img_res[i, j] = 1
    return img_res


def statistical_ciel(img_lab):
    return (
        np.mean(img_lab[:, :, 0]),
        np.mean(img_lab[:, :, 1]),
        np.mean(img_lab[:, :, 2]),
    )
