import math

import numpy as np

# 0-玻璃种
# 1-高冰种
# 2-冰种
# 3-冰糯种
# 4-糯化种
# 5-糯种
# 6-细豆种
# 7-豆种
import pandas as pd


def get_k(S_rank, ratio, zhong):
    '''

    :param S_rank:
    :param ratio:
    :param zhong:
    :return:
    '''
    if isinstance(zhong, int):
        pass
    elif isinstance(zhong, str):
        zhong2value = {'冰种': 2, '冰糯种': 3, '玻璃种': 0, '糯化种': 4, '糯种': 5, '细豆种': 6, '豆种': 7, '高冰种': 1}
        assert zhong in zhong2value.keys(), ValueError(f"{zhong}不在''玻璃种,高冰种,冰种,冰糯种,糯化种,糯种,细豆种,豆种")
        zhong = zhong2value[zhong]
    w = np.array(
        [-232993.3181477483, -46033.49507745176, 15456.169852744251, 4076535.2854407085, 224157.77940467306, -17957.867651124638, -3388469.8570660665, 65.84380590976338, 111331.09516350241, -21805.25949061224, 0.587686164549299, 1787.7933709526496, 256213.9080519916, -34.060378012456184, 30.836212590022114, -12920.055482617263])

    def rank_ratio_exp(a, b, c):
        return pow(S_rank, a) * pow(ratio, b) * pow(np.exp(-zhong), c)

    array = np.array([
        1,
        rank_ratio_exp(1, 0, 0),  # a
        rank_ratio_exp(0, 1, 0),  # b
        rank_ratio_exp(0, 0, 1),  # c

        rank_ratio_exp(2, 0, 0),  # a2
        rank_ratio_exp(1, 1, 0),  # ab
        rank_ratio_exp(1, 0, 1),  # ac
        rank_ratio_exp(0, 2, 0),  # b2
        rank_ratio_exp(0, 1, 1),  # bc
        # rank_ratio_exp(0, 0, 2),  # c2

        rank_ratio_exp(3, 0, 0),  # a3
        rank_ratio_exp(0, 3, 0),  # b3
        # rank_ratio_exp(0, 0, 3),  # c3
        rank_ratio_exp(2, 1, 0),  # a2b
        rank_ratio_exp(2, 0, 1),  # a2c
        rank_ratio_exp(1, 2, 0),  # ab2
        rank_ratio_exp(0, 2, 1),  # b2c
        # rank_ratio_exp(1, 0, 2),  # ac2
        # rank_ratio_exp(0, 1, 2),  # bc2
        rank_ratio_exp(1, 1, 1),  # abc
    ])
    return np.matmul(w, array) * math.exp(-zhong)


def caculate_ValueDegree(S_rank, ratio):
    '''

    :param S_rank:
    :param ratio:
    :return:
    '''

    w = np.array(
        [3949594.5419670288, 259.02730292161885, -54327.66517707645, 1060662.043658334, 144596.25935956897,
         -4191243.8823073683])

    def rank_ratio_exp(a, b):
        return ratio ** a * S_rank ** b

    array = np.array([
        1,
        rank_ratio_exp(2, 0),
        rank_ratio_exp(1, 1),
        rank_ratio_exp(0, 2),
        rank_ratio_exp(1, 0),
        rank_ratio_exp(0, 1)
    ])
    return (np.matmul(w, array) - 921821.287969931) / 11514323.862813503


# print(caculate_ValueDegree(1,100)-caculate_ValueDegree(3,0))
# print(caculate_ValueDegree(3, 5))
# print(get_k(1, 100, 0))
if __name__ == '__main__':
    a = pd.read_excel("手镯价格标准_all.xlsx")
    func = np.frompyfunc(get_k, 3, 1)
    rank = a["等级"]
    zhong = a["种"]
    ratio = a["比率"]
    price = func(rank, ratio, zhong)
    a["模型"] = price
    a.to_excel("手镯价格标准_all.xlsx",index=False)
    print(price)
    pass
