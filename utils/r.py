from utils.__init__ import binarizar, statistical_ciel, load_image
import numpy as np
from skimage.color import rgb2lab, rgba2rgb
from skimage import util
from matplotlib import pyplot as plt


def r1(img_lab, lm):
    return binarizar(img_lab, lm, 0)


def r2(img_lab, am):
    return binarizar(img_lab, am, 1)


def r3(img_lab, bm):
    return binarizar(img_lab, bm, 2)


def r4(img_lab):
    h, w, _ = img_lab.shape
    img_res = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            if img_lab[i, j, 2] >= img_lab[i, j, 1]:
                img_res[i, j] = 1
    return img_res


def test_rs():
    imagen_prueba = load_image("./images/sample2.jpg")
    img_paper1 = load_image("./images/paper_img1.png")
    img_paper2 = load_image("./images/paper_img2.png")

    img_paper1 = rgba2rgb(img_paper1)
    img_paper2 = rgba2rgb(img_paper2)
    img_paper1 = util.img_as_ubyte(img_paper1)
    img_paper2 = util.img_as_ubyte(img_paper2)

    img_lab0 = rgb2lab(imagen_prueba)
    img_lab1 = rgb2lab(img_paper1)
    img_lab2 = rgb2lab(img_paper2)

    lm, am, bm = statistical_ciel(img_lab0)
    r1_img = r1(img_lab0, lm)
    r2_img = r2(img_lab0, am)
    r3_img = r3(img_lab0, bm)
    r4_img = r4(img_lab0)

    lm1, am1, bm1 = statistical_ciel(img_lab1)
    r1_img1 = r1(img_lab1, lm1)
    r2_img1 = r2(img_lab1, am1)
    r3_img1 = r3(img_lab1, bm1)
    r4_img1 = r4(img_lab1)

    lm2, am2, bm2 = statistical_ciel(img_lab2)
    r1_img2 = r1(img_lab2, lm2)
    r2_img2 = r2(img_lab2, am2)
    r3_img2 = r3(img_lab2, bm2)
    r4_img2 = r4(img_lab2)

    fig, axes = plt.subplots(3, 5, figsize=(8, 8))
    ax = axes.ravel()

    ax[0].imshow(imagen_prueba)
    ax[1].imshow(r1_img, cmap=plt.cm.gray)  # R1
    ax[2].imshow(r2_img, cmap=plt.cm.gray)  # R2
    ax[3].imshow(r3_img, cmap=plt.cm.gray)  # R3
    ax[4].imshow(r4_img, cmap=plt.cm.gray)  # R4

    ax[5].imshow(img_paper1)
    ax[6].imshow(r1_img1, cmap=plt.cm.gray)  # R1
    ax[7].imshow(r2_img1, cmap=plt.cm.gray)  # R2
    ax[8].imshow(r3_img1, cmap=plt.cm.gray)  # R3
    ax[9].imshow(r4_img1, cmap=plt.cm.gray)  # R4

    ax[10].imshow(img_paper2)
    ax[11].imshow(r1_img2, cmap=plt.cm.gray)  # R1
    ax[12].imshow(r2_img2, cmap=plt.cm.gray)  # R2
    ax[13].imshow(r3_img2, cmap=plt.cm.gray)  # R3
    ax[14].imshow(r4_img2, cmap=plt.cm.gray)  # R4

    for a in ax:
        a.axis("off")

    ax[0].set_title("original")
    ax[1].set_title("R1")
    ax[2].set_title("R2")
    ax[3].set_title("R3")
    ax[4].set_title("R4")

    fig.tight_layout()
    plt.show()


def imprimir_rs_mask(imagen,r1,r2,r3,r4):
    and_img = np.logical_and(r1, r2)
    and_img = np.logical_and(and_img, r3)
    and_img = np.logical_and(and_img, r4)
    times_img=np.zeros_like(imagen)
    times_img[:,:,0]=and_img*imagen[:,:,0]
    times_img[:,:,1]=and_img*imagen[:,:,1]
    times_img[:,:,2]=and_img*imagen[:,:,2]

    fig, axes = plt.subplots(1, 3, figsize=(8, 8))
    ax = axes.ravel()
    ax[0].imshow(imagen)
    ax[0].axis('off')
    ax[1].imshow(and_img, cmap=plt.cm.gray)
    ax[1].axis('off')
    ax[2].imshow(times_img)
    ax[2].axis('off')


def test_rs_mask(img_path):

    img_paper1 = load_image(img_path)
    _,_,ch=img_paper1.shape

    if ch==4:
        img_paper1=rgba2rgb(img_paper1)
    img_paper1=util.img_as_ubyte(img_paper1)

    img_lab1 = rgba2rgb(img_paper1)

    lm1, am1, bm1 = statistical_ciel(img_lab1)
    r1_img1 = r1(img_lab1, lm1)
    r2_img1 = r2(img_lab1, am1)
    r3_img1 = r3(img_lab1, bm1)
    r4_img1 = r4(img_lab1)

    imprimir_rs_mask(img_paper1,r1_img1,r2_img1,r3_img1,r4_img1)
