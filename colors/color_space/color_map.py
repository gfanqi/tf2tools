from pprint import pprint

import numpy as np
import collections
import pandas as pd
from pypinyin import lazy_pinyin

colorname_cn2en = {
    "全色": "all_color",
    "墨翠": "mocui",
    "浅绿": "lightgreen",
    "绿色": "green",
    "蓝绿色": "bluegreen",
    "紫色": "purple"
}


def color_rank(path, compose_type="rank"):
    # path = "color_type_all_V3.xlsx"
    # path = "color_rank_all.xlsx"
    default_dict = collections.defaultdict(list)
    data = pd.read_excel(path)
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


if __name__ == '__main__':
    # a = S_green_jiadong()
    pprint(color_rank(path="color_rank_all_V1_2_1.xlsx"))
    # print(a)
