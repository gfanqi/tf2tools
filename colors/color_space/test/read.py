import math
from collections import Counter
from pprint import pprint

import cv2
import numpy as np

image = cv2.imread("./test.JPG")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


def show(hsv, mask=None):
    if mask == None:
        mask = np.ones(shape=hsv.shape[:2], dtype=np.bool)
    image = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
    pixs = hsv[mask > 0]
    pixs = [tuple(item) for item in pixs]
    pixs = np.array(list(set(pixs))) * np.array([2, 1 / 2.55, 1 / 2.55])
    center = [255, 255]
    H, W = image.shape[:2]
    # pixs = np.array([[1, 90, 90]])
    for pix in pixs:
        pix = pix / np.array([2, 1 / 2.55, 1 / 2.55])

        x = center[0] + pix[1] * math.sin(pix[0] / 180 * np.pi*2)
        y = center[0] + pix[1] * math.cos(pix[0] / 180 * np.pi*2)
        x = int(x)
        y = int(y)

        image[x, y] = np.array(pix)
    image = image.astype(np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.imshow("", image)
    # print(pixs)
    print(np.max(pixs, axis=0))
    print(np.min(pixs, axis=0))
    # # for pix in pixs:
    cv2.waitKey(0)


def stastic_colors(hsv, mask=None):
    if mask == None:
        mask = np.ones(shape=hsv.shape[:2], dtype=np.bool)
        pass
    hsv = hsv * np.array([2, 1 / 2.55, 1 / 2.55])
    pixs = hsv[mask > 0]
    pixs = [tuple(item) for item in pixs]
    counter = Counter(pixs)
    return counter


# pprint(stastic_colors(image))
show(image)
