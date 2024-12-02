import numpy as np
import math

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
