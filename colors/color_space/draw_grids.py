import collections
import math
import os
from pprint import pprint

import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import tqdm


colorname_cn2en = {
    "全色": "all_color",
    "墨翠": "mocui",
    "浅绿": "lightgreen",
    "绿色": "green",
    "蓝绿色": "bluegreen",
    "紫色": "purple"
}

def rainbowcolor(i, full, reverse=False):
    if reverse:
        i = full - i
    if i < full / 3:
        r = 255
        g = math.ceil(255 * 3 * i / full)
        b = 0
    elif i < full / 2:
        r = math.ceil(750 - i * (250 * 6 / full))
        g = 255
        b = 0
    elif i < full * 2 / 3:
        r = 0
        g = 255
        b = math.ceil(i * (250 * 6 / full) - 750)
    elif i < full * 5 / 6:
        r = 0
        g = math.ceil(1250 - i * (250 * 6 / full))
        b = 255
    else:
        r = math.ceil(150 * i * (6 / full) - 750)
        g = 0
        b = 255
    return [r, g, b]

def hsv_colorspace_polar(H=510, W=510, rate=1, depth=0, if_save=True):
    '''
    画极坐标色域
    :param H:
    :param W:
    :param rate:
    :param depth:
    :param if_save:
    :return:
    '''
    H = W = 510 * rate
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
    saturation = np.sqrt(X ** 2 + Y ** 2) / rate
    value = np.ones_like(hue) * depth
    hsv = np.stack([hue, saturation, value], axis=-1)
    hsv = hsv.astype(np.uint8)
    hsv[..., 2][saturation > 255] = 0
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    if if_save:
        cv2.imwrite("depth_{}.jpg".format(depth), bgr)
    return hsv, bgr


def coord_shift(h, s, center):
    h = h / 180 * math.pi * 2
    return int(center[0] + math.cos(h) * s), int(center[1] + math.sin(h) * s)


def draw_trapezoid(src, lowerb, upperb, center, color, thickness, depth, lineType=None, shift=None, rate=1):
    '''
    画椭圆弧形梯形
    :param src:
    :param lowerb:
    :param upperb:
    :param center:
    :param color:
    :param thickness:
    :param depth:
    :param lineType:
    :param shift:
    :param rate:
    :return:
    '''
    img = src.copy()
    (h_min, h_max), (s_min, s_max), (v_min, v_max) = list(zip(lowerb, upperb))
    # print(src, lowerb, upperb, center, color, thickness, depth, )
    # exit()
    if depth > v_max or depth < v_min: return img
    cv2.ellipse(img=img, center=center, axes=((s_min + 1) * rate, (s_min + 1) * rate), angle=0, startAngle=h_min * 2,
                endAngle=h_max * 2, color=color, thickness=thickness * rate, lineType=lineType, shift=shift)
    cv2.ellipse(img=img, center=center, axes=((s_max - 1) * rate, (s_max - 1) * rate), angle=0, startAngle=h_min * 2,
                endAngle=h_max * 2, color=color, thickness=thickness * rate, lineType=lineType, shift=shift)
    pt1 = coord_shift(h_min, (s_min + 1) * rate, center)
    pt2 = coord_shift(h_min, (s_max - 1) * rate, center)
    cv2.line(img=img, pt1=pt1, pt2=pt2, color=color, thickness=thickness * rate, lineType=lineType, shift=shift)
    pt1 = coord_shift(h_max, (s_min + 1) * rate, center)
    pt2 = coord_shift(h_max, (s_max - 1) * rate, center)
    cv2.line(img=img, pt1=pt1, pt2=pt2, color=color, thickness=thickness * rate, lineType=lineType, shift=shift)
    return img


def choose_color_range(mask, lowerb, upperb, color=(0, 0, 255), depth=None, thickness=2, rate=1):
    '''
    选择颜色范围，画弧梯形
    :param mask:
    :param lowerb:
    :param upperb:
    :param color:
    :param depth:
    :param thickness:
    :param rate:
    :return:
    '''
    H, W = mask.shape[:2]
    center = (int(H / 2), int(W / 2))
    center = center[::-1]
    # bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    mask = draw_trapezoid(mask, lowerb, upperb, center, color, thickness=thickness, depth=depth, rate=rate)
    # hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    return mask



def color_rank(color_range_path, compose_type="rank"):

    default_dict = collections.defaultdict(list)
    data = pd.read_excel(color_range_path)
    data = data.reset_index(drop=True)
    df = data.dropna()
    name = "name" if compose_type == "rank" else "颜色"
    for i in range(len(df)):
        # print(df)
        rankwithindex = df.loc[i, name]
        if compose_type == "rank":
            rank = rankwithindex
        else:
            rank = colorname_cn2en.get(rankwithindex,rankwithindex)
        color_range = df.loc[i, ["Hmin", "Hmax", "Smin", "Smax", "Vmin", "Vmax"]].tolist()
        color_range = [[color_range[2 * i], color_range[2 * i + 1]] for i in range(3)]
        color_range = np.array(color_range).T
        default_dict[rank] = default_dict.get(rank, [])
        default_dict[rank].append((color_range[0], color_range[1]))
    return default_dict
#
# def hsv_color_space(color_dict, name, h_num, s_num, v_num, grid_size=40, use_grid=False):
#     '''
#
#     :param color_dict:
#     :param name:
#     :param h_num:
#     :param s_num:
#     :param v_num:
#     :param grid_size:
#     :param use_grid:
#     :return:
#     '''
#     down, up = color_dict[name]
#     h = np.linspace(down[0], up[0], num=h_num, )
#     s = np.linspace(down[1], up[1], num=s_num, )
#     v = np.linspace(down[2], up[2], num=v_num, )
#     h = h / 2
#     s = s * 2.55
#     v = v * 2.55
#     c = np.meshgrid(h, s, v)
#     c = np.stack(c, axis=-1)
#     num_channel = c.shape[:3]
#     min_index = num_channel.index(min(num_channel))
#     c = np.swapaxes(c, axis1=0, axis2=min_index)
#     grid = None
#     if use_grid:
#         black_bar = np.zeros(shape=(grid_size, grid_size))
#         black_line_size = min(1, grid_size * 0.2)
#         black_bar[:black_line_size, :, ...] = 1
#         black_bar[:, :black_line_size, ...] = 1
#         grid = np.tile(black_bar, c.shape[1:3])
#     c = np.repeat(c, grid_size, axis=1)
#     c = np.repeat(c, grid_size, axis=2)
#     c = c.astype(np.uint8)
#     all_map = []
#     for i in range(min(num_channel)):
#         hsv = c[i]
#         rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
#         # print()
#         if use_grid:
#             rgb[grid > 0] = 0
#         # all_map.append(rgb)
#         # final = np.concatenate(all_map, axis=1)
#         cv2.imwrite("hv/depth_{}.jpg".format(int(i * 25.5)), rgb)
#     # return final



# print(color_dict)

def color_range_visilization(color_range_path = "color_rank_all_V1_2_1.xlsx",compose_type = "rank",rate=2,V_step = -5,name = "test"):
    color_range = color_rank(compose_type=compose_type,color_range_path=color_range_path)
    # color = [(key, rainbowcolor(index, 7)) for index, key in enumerate(color_range.keys())]
    color = [(f"S{i}", rainbowcolor(i, 5, reverse=False)) for i in range(0, 6)]
    # color = [("S{}_green".format(i), rainbowcolor(i - 1, 7, reverse=False)) for i in range(1, 5)]
    # color.append(("S{}_S5".format(5), rainbowcolor(4, 7, reverse=False)))
    rainbow_color_dict = dict(color)

    color_map = np.zeros(shape=(40 * len(rainbow_color_dict) * rate, 200 * rate, 3), dtype=np.uint8)
    for i, l2color in enumerate(rainbow_color_dict):
        # print(l2color)
        cv2.putText(color_map, text=l2color, org=(5 * rate, (40 * i + 20) * rate), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5 * rate,
                    color=(255, 255, 255), thickness=1 * rate)
        cv2.rectangle(color_map, pt1=(100 * rate, (40 * i + 20) * rate), pt2=(196 * rate, (40 * i + 10) * rate),
                      color=rainbow_color_dict[l2color][::-1],
                      thickness=-1)
        pass
    # cv2.imshow("", color_map)
    # cv2.waitKey(2000)
    color_dict = color_range.copy()
    for depth in tqdm.tqdm(range(100, 0, V_step)):
        hsv, bgr = hsv_colorspace_polar(rate=rate, depth=int(depth * 2.55), if_save=False)
        # hsv = hsv.copy()
        # cv2.imshow("", bgr)
        # cv2.waitKey(0)
        img = np.zeros_like(hsv, dtype=np.uint8)
        img = np.pad(img, pad_width=((40 * rate, 40 * rate), (40 * rate, 40 * rate), (0, 0)))
        H, W = img.shape[:2]
        center = (H // 2, W // 2)
        for r in range(0, 360, 10):
            x = center[0] + (W / 2 * 0.95) * math.cos(r / 180 * np.pi)
            y = center[0] + (W / 2 * 0.95) * math.sin(r / 180 * np.pi)
            x = int(x) - 17 * rate
            y = int(y) + 10 * rate
            cv2.putText(img, "{}".format(r), (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5 * rate,
                        color=(0, 0, 255), thickness=1 * rate)
        img = cv2.line(img=img, pt1=(40 * rate, H // 2), pt2=(W - 40 * rate, H // 2), color=(255, 200, 200),
                       thickness=1 * rate)
        img = cv2.line(img=img, pt1=(40 * rate, H // 2), pt2=(W - 40 * rate, H // 2), color=(255, 200, 200),
                       thickness=1 * rate)
        # cv2.imshow("", img)
        # cv2.waitKey(0)
        for i in range(36):
            pt2 = int(center[0] + math.cos(i * 10 / 180 * np.pi) * (W // 2 - 40 * rate)), int(
                center[1] + math.sin(i * 10 / 180 * np.pi) * (W // 2 - 40 * rate))
            cv2.line(img, pt1=center, pt2=pt2, color=(255, 200, 200), thickness=1 * rate)

        for key in color_dict:

            for lowerb, upperb in color_dict[key]:
                lowerb = lowerb * np.array([0.5, 2.55, 2.55])
                upperb = upperb * np.array([0.5, 2.55, 2.55])
                # print(lowerb, upperb)
                lowerb = lowerb.astype(np.int)
                upperb = upperb.astype(np.int)
                # l2key = "_".join(key.split("_")[:2])
                l2key = key.split("-")[0]
                img[40 * rate:-40 * rate, 40 * rate:-40 * rate, ] = choose_color_range(
                    img[40 * rate:-40 * rate, 40 * rate:-40 * rate, ], lowerb=lowerb, upperb=upperb,
                    color=rainbow_color_dict[l2key][::-1],
                    depth=int(depth * 2.55), rate=rate)
        # break
        for i in range(-10, 10 + 1):
            if i > 0:
                cv2.circle(img, center=center, radius=int((W // 2 - 40 * rate) / 10 * i), thickness=1 * rate,
                           color=(255, 200, 200))
            pt1 = (int(center[0] + (W - 80 * rate) // 2 / 10 * i), center[1])
            pt2 = (pt1[0], center[0] - 5)
            img = cv2.line(img, pt1, pt2, color=(255, 200, 200), thickness=1 * rate)
            cv2.putText(img, text=f"{abs(i) * 10}", org=(pt2[0] - 4, pt2[1] - 2), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.3 * rate,
                        color=(0, 1, 0), thickness=1 * rate)

        # cv2.imshow("", img)
        # cv2.waitKey(0)
        # if not os.path.exists("S1_green"): os.mkdir("S1_green")
        # img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

        # img[]
        bgr = np.pad(bgr, pad_width=((40 * rate, 40 * rate), (40 * rate, 40 * rate), (0, 0)))
        # img = np.pad(img, pad_width=((40, 40), (40, 40), (0, 0)))

        mask = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bgr[mask > 0] = img[mask > 0]
        # bgr = img.copy()
        pad_h = bgr.shape[0] - color_map.shape[0]
        color_map = np.pad(color_map, pad_width=((pad_h // 2, pad_h - pad_h // 2), (0, 0), (0, 0)))
        cv2.rectangle(color_map, pt1=(38 * rate, 105 * rate), pt2=(140 * rate, 60 * rate), color=(0, 0, 0),
                      thickness=-1)
        cv2.putText(color_map, "B={}".format(int(depth)), org=(40 * rate, 100 * rate),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.8 * rate, color=(255, 255, 255), thickness=2 * rate)
        bgr = np.concatenate([bgr, color_map], axis=-2)
        if not os.path.exists("S_green_{}".format(name)): os.makedirs("S_green_{}".format(name))
        cv2.imwrite(os.path.join("S_green_{}".format(name), "{}_B.jpg".format(int(depth))), bgr)
        print("\rdone",end="")

if __name__ == '__main__':
    color_range_visilization()
