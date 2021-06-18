import cv2
import numpy as np


def is_avail(x, min_=None, max_=None):
    '''
    if the value x has range,use this function to make sure that x is in the range.
    :param x:
    :param min_:
    :param max_:
    :return:
    '''
    low_bound = True
    high_bound = True
    if min_ is not None:
        low_bound = x >= min_
    if max_ is not None:
        high_bound = x <= max_
    return low_bound and high_bound



def hsv_corlor_selector(min_H=0, max_H=180, min_S=0, max_S=255, min_V=0, max_V=255, select_red=False):
    '''
    corlor selector
    :param min_H:
    :param max_H:
    :param min_S:
    :param max_S:
    :param min_V:
    :param max_V:
    :return:
    '''
    assert is_avail(min_H, 0, 180)
    assert is_avail(max_H, 0, 180)
    assert is_avail(min_S, 0, 255)
    assert is_avail(max_S, 0, 255)
    assert is_avail(min_V, 0, 255)
    assert is_avail(max_V, 0, 255)
    assert min_H <= max_H and min_S <= max_S and min_V < max_V

    def selector(hsv_img, min_H=min_H, max_H=max_H, min_S=min_S, max_S=max_S, min_V=min_V, max_V=max_V):
        if select_red:
            mask_h = np.logical_or(hsv_img[..., 0] <= min_H, hsv_img[..., 0] >= max_H)
        else:
            mask_h = np.logical_and(hsv_img[..., 0] >= min_H, hsv_img[..., 0] <= max_H)
        mask_s = np.logical_and(hsv_img[..., 1] >= min_S, hsv_img[..., 1] <= max_S)
        mask_v = np.logical_and(hsv_img[..., 2] >= min_V, hsv_img[..., 2] <= max_V)
        mask = mask_h * mask_s * mask_v
        mask = mask.astype(np.bool)
        return mask
    return selector


black_selector = hsv_corlor_selector(0, 180, 0, 255, 0, 46)
gray_selector = hsv_corlor_selector(0, 180, 0, 43, 46, 220)
white_selector = hsv_corlor_selector(0, 180, 0, 30, 221, 255)
red_selector = hsv_corlor_selector(10, 156, 43, 255, 46, 255, True)
orange_selector = hsv_corlor_selector(11, 25, 43, 255, 46, 255)
yellow_selector = hsv_corlor_selector(26, 34, 43, 255, 46, 255)
green_selector = hsv_corlor_selector(35, 77, 43, 255, 46, 255)
cyan_selector = hsv_corlor_selector(78, 99, 43, 255, 46, 255)
blue_selector = hsv_corlor_selector(100, 124, 43, 255, 46, 255)
purple_selector = hsv_corlor_selector(125, 155, 43, 255, 46, 255)

