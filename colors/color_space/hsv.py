import collections
import math
import os
from pprint import pprint

import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd

from colors.color_space.color_map import S_green_jiadong, S_green_fanqi
from colors.rainbow.rainbow_color import rainbowcolor


def hsv_colorspace_polar(H=510, W=510, depth=0, if_save=True):
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
    saturation = np.sqrt(X ** 2 + Y ** 2)
    value = np.ones_like(hue) * depth
    hsv = np.stack([hue, saturation, value], axis=-1)
    hsv = hsv.astype(np.uint8)
    hsv[..., 2][saturation > 255] = 64
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    if if_save:
        cv2.imwrite("depth_{}.jpg".format(depth), bgr)
    return hsv, bgr


def coord_shift(h, s, center):
    h = h / 180 * math.pi * 2
    return int(center[0] + math.cos(h) * s), int(center[1] + math.sin(h) * s)


def draw_trapezoid(src, lowerb, upperb, center, color, thickness, depth, lineType=None, shift=None):
    img = src.copy()
    (h_min, h_max), (s_min, s_max), (v_min, v_max) = list(zip(lowerb, upperb))
    # print(src, lowerb, upperb, center, color, thickness, depth, )
    # exit()
    if depth > v_max or depth < v_min: return img
    cv2.ellipse(img=img, center=center, axes=(s_min, s_min), angle=0, startAngle=h_min * 2,
                endAngle=h_max * 2, color=color, thickness=thickness, lineType=lineType, shift=shift)
    cv2.ellipse(img=img, center=center, axes=(s_max, s_max), angle=0, startAngle=h_min * 2,
                endAngle=h_max * 2, color=color, thickness=thickness, lineType=lineType, shift=shift)
    pt1 = coord_shift(h_min, s_min, center)
    pt2 = coord_shift(h_min, s_max, center)
    cv2.line(img=img, pt1=pt1, pt2=pt2, color=color, thickness=thickness, lineType=lineType, shift=shift)
    pt1 = coord_shift(h_max, s_min, center)
    pt2 = coord_shift(h_max, s_max, center)
    cv2.line(img=img, pt1=pt1, pt2=pt2, color=color, thickness=thickness, lineType=lineType, shift=shift)
    return img


def choose_color_range(hsv, lowerb, upperb, color=(0, 0, 255), depth=None, thickness=2):
    H, W = hsv.shape[:2]
    center = (int(H / 2), int(W / 2))
    center = center[::-1]
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    bgr = draw_trapezoid(bgr, lowerb, upperb, center, color, thickness=thickness, depth=depth)
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    return hsv


def hsv_color_space(color_dict, name, h_num, s_num, v_num, grid_size=40, use_grid=False):
    # rows =
    down, up = color_dict[name]
    h = np.linspace(down[0], up[0], num=h_num, )
    s = np.linspace(down[1], up[1], num=s_num, )
    v = np.linspace(down[2], up[2], num=v_num, )
    h = h / 2
    s = s * 2.55
    v = v * 2.55
    c = np.meshgrid(h, s, v)
    c = np.stack(c, axis=-1)
    num_channel = c.shape[:3]
    min_index = num_channel.index(min(num_channel))
    c = np.swapaxes(c, axis1=0, axis2=min_index)
    grid = None
    if use_grid:
        black_bar = np.zeros(shape=(grid_size, grid_size))
        black_line_size = min(1, grid_size * 0.2)
        black_bar[:black_line_size, :, ...] = 1
        black_bar[:, :black_line_size, ...] = 1
        grid = np.tile(black_bar, c.shape[1:3])
    c = np.repeat(c, grid_size, axis=1)
    c = np.repeat(c, grid_size, axis=2)
    c = c.astype(np.uint8)
    all_map = []
    for i in range(min(num_channel)):
        hsv = c[i]
        rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        # print()
        if use_grid:
            rgb[grid > 0] = 0
        # all_map.append(rgb)
        # final = np.concatenate(all_map, axis=1)
        cv2.imwrite("hv/depth_{}.jpg".format(int(i * 25.5)), rgb)
    # return final


color = [("S{}_green".format(i), rainbowcolor(i, 7, reverse=True)) for i in range(6)]
color.append(("S{}_S5".format(5), rainbowcolor(5, 7, reverse=True)))
rainbow_color_dict = dict(color)
# print(color_dict)
if __name__ == '__main__':
    for name in ["fanqi","jiadong"]:
        color_dict = S_green_jiadong() if name == "jiadong" else S_green_fanqi()
        # color_dict["all"] = [np.array([60, 0, 0]), np.array([180, 100, 100])]
        # hsv_color_space(color_dict, "all", 50, 50, 10, )
        for depth in range(0, 255, 10):
            hsv, bgr = hsv_colorspace_polar(depth=depth, if_save=False)
            img = hsv.copy()
            for key in color_dict:
                # if not os.path.exists(key): os.mkdir(key)
                lowerb, upperb = color_dict[key]
                # print(lowerb)
                lowerb = lowerb * np.array([0.5, 2.55, 2.55])
                upperb = upperb * np.array([0.5, 2.55, 2.55])
                lowerb = lowerb.astype(np.int)
                upperb = upperb.astype(np.int)
                l2key = "_".join(key.split("_")[:2])
                img = choose_color_range(img, lowerb=lowerb, upperb=upperb, color=rainbow_color_dict[l2key], depth=depth)
            # if not os.path.exists("S1_green"): os.mkdir("S1_green")
            img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
            img = np.pad(img, pad_width=((40, 40), (40, 40), (0, 0)))
            H, W = img.shape[:2]
            center = (H // 2, W // 2)
            for r in range(0, 360, 10):
                x = center[0] + (W / 2 * 0.95) * math.cos(r / 180 * np.pi)
                y = center[0] + (W / 2 * 0.95) * math.sin(r / 180 * np.pi)
                x = int(x)-20
                y = int(y)+10
                cv2.putText(img, "{}".format(r), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            cv2.imwrite(os.path.join("S1_green_{}".format(name), "depth_{}.jpg".format(int(depth / 2.55))), img)
