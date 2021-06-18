import math

import cv2
import numpy as np

# def RG
import tqdm


def rgb2greencenter(img):
    src = np.array([[0, 0, 0],  # 黑
                    [255, 0, 0],  # 红
                    [0, 255, 0],  # 绿
                    [0, 0, 255],
                    [255, 255, 255]], dtype=np.uint8)  # 蓝
    src = src/255
    r = np.pi / 4
    Rx = np.array([[1, 0, 0],
                   [0, math.cos(r), -math.sin(r)],
                   [0, math.sin(r), math.cos(r)]])
    # r = math.asin(-1/math.sqrt(3))
    r = np.pi / 4
    Ry = np.array([[math.cos(r), 0, math.sin(r)],
                   [0, 1, 0],
                   [-math.sin(r), 0, math.cos(r)]])
    # print(np.matmul(src,Rx, ))
    src = np.mat(src)
    Rx = np.mat(Rx)
    print(Rx.shape)
    print(src.shape)
    print(src*Ry)
    # print(src)
    # print(a)
    pass


print(rgb2greencenter(None))
exit()
# def show_lab_color_spase():
#     L = np.arange(0, 255)
#     a = np.arange(0, 255)
#     b = np.arange(0, 255)
#     X, Y, Z = np.meshgrid(L, a, b)
#
#     # exit()
#
#     colors = np.stack([X, Y, Z], axis=-1)
#     for i in range(0, 255, 1):
#         # lab = colors[i, :, :, ...]
#         # lab = colors[:, i, :, ...]
#         lab = colors[:, :, i, ...]
#         lab = lab.astype(np.uint8)
#         bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
#         cv2.imshow("", bgr)
#         cv2.waitKey(2)
#     pass
import matplotlib.pyplot as plt


def hsv_colorspace_polar(H=1500, W=1500, depth=0, if_save=True):
    center = (H // 2, W // 2)
    floor_center = center
    X, Y = np.meshgrid(range(H), range(W))
    X = X - center[0]
    Y = Y - center[1]
    X = X + 1e-15
    hue = np.arctan(Y / X) / np.pi * 180
    hue[:, :floor_center[1]] = hue[:, :floor_center[1]] + 180
    hue[:, floor_center[1]:] = hue[:, floor_center[1]:] + 360
    hue = hue / 2
    saturation = np.sqrt(X ** 2 + Y ** 2) / W / 0.9 * 255 * 2
    value = np.ones_like(hue) * depth
    hsv = np.stack([hue, saturation, value], axis=-1)
    hsv[..., 0] = hsv[..., 0] // 2 * 2
    # hsv[..., 1] = hsv[..., 1] // 5 * 5
    hsv[..., 2] = hsv[..., 2] // 5 * 5

    # hsv[..., 1] = hsv[..., 1] * 0.9
    hsv[..., 1] = saturation * ((-np.cos(hue * 2 * np.pi / 180 * 3) + 3.5) / 4.5)
    # plt.imshow(hsv[...,1] )
    # plt.show()
    # input()
    # hsv[...,1] = saturation*((-np.cos(hue * np.pi / 180*3)+5))
    # hue = np.arange(0, 360)
    # plt.plot(np.arange(360),(-np.cos(hue * np.pi / 180*3)+3.5)/4.5, )
    # plt.show()
    # input()
    # print(np.sin(np.pi))

    # plt.plot(Xs, Ys)
    # plt.show()
    # input()
    hsv = hsv.astype(np.uint8)
    # hsv[..., 2][saturation > 255] = 0
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    # bgr = bgr * (np.array([1, -1, 1])) + (np.array([0, 255, 0]),)
    bgr = bgr * (np.array([-1, 1, -1])) + (np.array([255, 0, 255]),)
    bgr = bgr.astype(np.uint8)
    bgr[saturation > 255] = 0

    for r in range(0, 360, 5):
        X = center[0] - 10 + (W / 2 * 0.95) * math.cos(r / 180 * np.pi)
        Y = center[0] + (W / 2 * 0.95) * math.sin(r / 180 * np.pi)
        X = int(X)
        Y = int(Y)
        cv2.putText(bgr, "{}".format(r), (X, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    for r in range(0, W // 2, W // 20):
        cv2.circle(bgr, center=center, radius=r, color=(0, 0, 0), thickness=3)
        cv2.putText(bgr, "{}".format(r), (X, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    # X = np.arange(0, 360)
    # Y = (-(np.cos(X * np.pi / 180 * 3)**2*np.sin(X * np.pi / 180 * 3))*3 + 4) / 5 * H / 3
    # Xs = Y * np.sin(X * np.pi / 180) + center[0]
    # Ys = Y * np.cos(X * np.pi / 180) + center[1]
    # Xs = Xs.astype(np.int)
    # Ys = Ys.astype(np.int)

    # bgr[Xs, Ys] = 255 - bgr[Xs, Ys]
    # cv2.imshow("",bgr)
    # cv2.waitKey(0)

    if if_save:
        cv2.imwrite("new/depth_{}.jpg".format(depth), bgr)
    return hsv, bgr


if __name__ == '__main__':
    # a = green_center_color_space()
    for i in tqdm.tqdm(range(240, 260, 5)):
        hsv_colorspace_polar(depth=i)
    # print()
