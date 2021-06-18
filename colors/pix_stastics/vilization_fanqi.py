from pprint import pprint
from random import random

import pandas as pd
import os
import numpy as np
import math
import cv2
from mayavi import mlab
from mayavi.tools.decorations import axes, outline
from mayavi.tools.helper_functions import test_points3d

from colors.color_space.color_map import S_green_jiadong, S_green_fanqi


def show2(lower_hsv: list, upper_hsv: list):
    h_range = [lower_hsv[0], upper_hsv[0]]
    s_range = [lower_hsv[1], upper_hsv[1]]
    v_range = [lower_hsv[2], upper_hsv[2]]

    h = np.linspace(h_range[0], h_range[1], endpoint=True, num=5)
    s = np.linspace(s_range[0], s_range[1], endpoint=True, num=5)
    v = np.linspace(v_range[0], v_range[1], endpoint=True, num=5)
    h, s, v = np.meshgrid(h, s, v)
    h = h.flatten()
    s = s.flatten()
    v = v.flatten()

    center = (255, 255, 255)
    x = center[0] + s * np.sin(h / 180 * np.pi + np.pi / 2)
    y = center[1] + s * np.cos(h / 180 * np.pi + np.pi / 2)
    z = (v)
    x = x.astype(np.int)
    y = y.astype(np.int)
    z = z.astype(np.int)
    return x, y, z


all_keys = list(S_green_fanqi().keys()) + list(S_green_jiadong().keys())
# show2()
all_keys = set(all_keys)
# print(all_keys)
total = {}
for item in all_keys:
    l2name = "_".join(item.split("_")[:2])
    total[l2name] = total.get(l2name, []) + [item]

pprint(total)


def visualize(S_green):
    # for S_green in [S_green_fanqi(),S_green_jiadong()]:
    # S_green =  S_green_fanqi() if  "fanqi"
    xs, ys, zs, labels = [], [], [], []
    for index, l2key in enumerate(total):
        l3names = total[l2key]

        for l3name in l3names:
            lower_hsv, upper_hsv = S_green.get(l3name, [None, None])
            if lower_hsv is None: continue
            x, y, z = show2(lower_hsv, upper_hsv)
            xs.append(x)
            ys.append(y)
            zs.append(z)
            label = [index + 0.4 * random()] * x.shape[0]
            # print(len(label))
            labels.extend(label)
        # print(len(xs))
    xs = np.concatenate(xs, axis=-1)
    ys = np.concatenate(ys, axis=-1)
    zs = np.concatenate(zs, axis=-1)
    # print(dir(mlab))
    print(mlab.points3d.__doc__)
    mlab.points3d(xs, ys, zs, mode='point', resolution=10, name="fanqi", line_width=8,
                  colormap=[(1.0, 0.0, 0.0)] * xs.shape[0])

    axes(xlabel='X', ylabel='Y', zlabel='Z')
    mlab.show()
    # pass


visualize(S_green_fanqi())

exit()


def show(hsv, mask=None):
    if mask == None:
        mask = np.ones(shape=hsv.shape[:2], dtype=np.bool)
    image = np.zeros(shape=(512, 512, 512, 3), dtype=np.uint8)
    pixs = hsv * np.array([2, 1, 1])
    center = [255, 255]
    x = center[0] + pixs[..., 1] * np.sin(-pixs[..., 0] / 180 * np.pi)
    y = center[0] + pixs[..., 1] * np.cos(-pixs[..., 0] / 180 * np.pi)
    z = (pixs[..., 2])
    x = x.astype(np.int)
    y = y.astype(np.int)
    z = z.astype(np.int)
    # image[x, y, z] = 255
    return x, y, z


# df = pd.read_csv
l2names = ["_".join(item.split("_")[:2]) for item in os.listdir("./pixs")]
# for l2name
total = {}
for item in os.listdir("./pixs"):
    l2name = "_".join(item.split("_")[:2])
    path = os.path.join("./pixs", item)
    total[l2name] = total.get(l2name, []) + [path]

l2keys = [
    'S4_红-黄色',
    'S1_绿色',
    # 'S2_绿色',
    # 'S3_绿色',
    # 'S4_绿色',
    # 'S1_紫色',
    # 'S2_紫色',
    # 'S3_紫色',
    # 'S3_红色',
    # 'S3_黄色',
    # 'S4_白色',
    # 'S4_紫色',
    # 'S4_红-黄色',
    'S5_S5'
]
# pprint(total.keys())
# exit()
xs = []
ys = []
zs = []
labels = []
for index, l2name in enumerate(l2keys):
    dfs = [pd.read_csv(df_path, index_col=[0]) for df_path in total.get(l2name)]
    df = pd.concat(dfs, ignore_index=True)
    print(len(df))
    pixs = df[["h", "s", "v"]].values
    x, y, z = show(hsv=pixs)
    xs.append(x)
    ys.append(y)
    zs.append(z)
    labels.extend([index + 1] * x.shape[0])
xs = np.concatenate(xs, axis=-1)
ys = np.concatenate(ys, axis=-1)
zs = np.concatenate(zs, axis=-1)
# mlab.points3d
print(len(xs))
# print(xs)
# // 10 * 10
# // 10 * 10
# // 10 * 10
xs = xs
ys = ys
zs = zs
# pixs = list(zip(xs, ys, zs, labels))
# pixs = [tuple(item) for item in pixs]
# pixs = set(pixs)
# xs = [pix[0] for pix in pixs]
# ys = [pix[1] for pix in pixs]
# zs = [pix[2] for pix in pixs]
# labels = [pix[3] for pix in pixs]
# print(np.max(zs))
print(xs)
print(ys)
print(zs)
print(labels)

l = mlab.points3d(xs, ys, zs, labels)
axes(xlabel='X', ylabel='Y', zlabel='Z')
outline(l)
# mlab.
# test_points3d()
mlab.show()
