import numpy as np
import collections
def S_green_jiadong():
    default_dict = collections.defaultdict(list)
    # S1
    lower_hsv = np.array([70, 80, 30])
    upper_hsv = np.array([130, 100, 100])
    default_dict['S1_green_1'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([130, 85, 30])
    upper_hsv = np.array([145, 100, 100])
    default_dict['S1_green_2'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([130, 65, 40])
    upper_hsv = np.array([145, 84, 100])
    default_dict['S1_green_3'] = [lower_hsv, upper_hsv]


    ##################################################
    lower_hsv = np.array([130, 40, 30])
    upper_hsv = np.array([145, 90, 100])
    default_dict['S2_green_1'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([80, 40, 45])
    upper_hsv = np.array([130, 60, 100])
    default_dict['S2_green_2'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([145, 45, 40])
    upper_hsv = np.array([210, 100, 100])
    default_dict['S2_green_3'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([145, 80, 30])
    upper_hsv = np.array([210, 100, 100])
    default_dict['S2_green_4'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([80, 60, 30])
    upper_hsv = np.array([130, 80, 100])
    default_dict['S2_green_5'] = [lower_hsv, upper_hsv]

    ##################################################
    lower_hsv = np.array([80, 30, 11])
    upper_hsv = np.array([145, 100, 33])
    default_dict['S3_green_1'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([130, 30, 0])
    upper_hsv = np.array([145, 100, 10])
    default_dict['S3_green_2'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([145, 30, 34])
    upper_hsv = np.array([210, 100, 59])
    default_dict['S3_green_3'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([145, 30, 60])
    upper_hsv = np.array([210, 49, 100])
    default_dict['S3_green_4'] = [lower_hsv, upper_hsv]


    lower_hsv = np.array([70, 6, 34])
    upper_hsv = np.array([130, 30, 100])
    default_dict['S4_green_1'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([130, 6, 11])
    upper_hsv = np.array([145, 30, 100])
    default_dict['S4_green_2'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([145, 6, 34])
    upper_hsv = np.array([210, 30, 100])
    default_dict['S4_green_3'] = [lower_hsv, upper_hsv]
    lower_hsv = np.array([215, 6, 0])
    upper_hsv = np.array([360, 100, 10])
    default_dict['S5_S5_1'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([0, 6, 0])
    upper_hsv = np.array([145, 100, 10])
    default_dict['S5_S5_2'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([116, 6, 11])
    upper_hsv = np.array([145, 23, 33])
    default_dict['S5_S5_3'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([145, 6, 0])
    upper_hsv = np.array([210, 79, 33])
    default_dict['S5_S5_4'] = [lower_hsv, upper_hsv]

    return default_dict


def S_green_fanqi():
    default_dict = collections.defaultdict(list)
    # S1
    lower_hsv = np.array([90, 80, 33])
    upper_hsv = np.array([130, 100, 100])
    default_dict['S1_green_1'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([130, 80, 33])
    upper_hsv = np.array([145, 100, 100])
    default_dict['S1_green_2'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([110, 60, 40])
    upper_hsv = np.array([145, 80, 100])
    default_dict['S1_green_3'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([130, 40, 33])
    upper_hsv = np.array([145, 60, 100])
    default_dict['S2_green_1'] = [lower_hsv, upper_hsv]

    # lower_hsv = np.array([70, 40, 30])
    # upper_hsv = np.array([130, 80, 100])
    # default_dict['S2_green_2'] = [lower_hsv, upper_hsv]
    lower_hsv = np.array([85, 40, 45])
    upper_hsv = np.array([130, 60, 100])
    default_dict['S2_green_2'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([145, 40, 60])
    upper_hsv = np.array([160, 100, 100])
    default_dict['S2_green_3'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([145, 80, 60])
    upper_hsv = np.array([160, 100, 100])
    default_dict['S2_green_4'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([85, 60, 33])
    upper_hsv = np.array([110, 80, 100])
    default_dict['S2_green_5'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([110, 60, 33])
    upper_hsv = np.array([145, 80, 40])
    default_dict['S2_green_6'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([160, 40, 60])
    upper_hsv = np.array([190, 100, 100])
    default_dict['S2_green_7'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([80, 30, 11])
    upper_hsv = np.array([190, 100, 33])
    default_dict['S3_green_1'] = [lower_hsv, upper_hsv]



    lower_hsv = np.array([160, 30, 33])
    upper_hsv = np.array([180, 100, 59])
    default_dict['S3_green_2'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([80, 30, 30])
    upper_hsv = np.array([190, 40, 100])
    default_dict['S3_green_3'] = [lower_hsv, upper_hsv]

    # lower_hsv = np.array([145, 40, 33])
    # upper_hsv = np.array([160, 100, 50])
    # default_dict['S3_green_3'] = [lower_hsv, upper_hsv]

    lower_hsv = np.array([145, 40, 30])
    upper_hsv = np.array([190, 100, 60])
    default_dict['S3_green_4'] = [lower_hsv, upper_hsv]

    # lower_hsv = np.array([160, 40, 30])
    # upper_hsv = np.array([190, 100, 60])
    # default_dict['S3_green_5'] = [lower_hsv, upper_hsv]
    #
    # lower_hsv = np.array([70, 6, 34])
    # upper_hsv = np.array([130, 30, 100])
    # default_dict['S4_green_1'] = [lower_hsv, upper_hsv]
    #
    # lower_hsv = np.array([130, 6, 11])
    # upper_hsv = np.array([145, 30, 100])
    # default_dict['S4_green_2'] = [lower_hsv, upper_hsv]
    #
    # lower_hsv = np.array([145, 6, 34])
    # upper_hsv = np.array([210, 30, 100])
    # default_dict['S4_green_3'] = [lower_hsv, upper_hsv]
    #
    # lower_hsv = np.array([215, 6, 0])
    # upper_hsv = np.array([360, 100, 10])
    # default_dict['S5_S5_1'] = [lower_hsv, upper_hsv]
    #
    # lower_hsv = np.array([0, 6, 0])
    # upper_hsv = np.array([145, 100, 10])
    # default_dict['S5_S5_2'] = [lower_hsv, upper_hsv]
    #
    # lower_hsv = np.array([116, 6, 11])
    # upper_hsv = np.array([145, 23, 33])
    # default_dict['S5_S5_3'] = [lower_hsv, upper_hsv]
    #
    # lower_hsv = np.array([145, 6, 0])
    # upper_hsv = np.array([215, 100, 33])
    # default_dict['S5_S5_4'] = [lower_hsv, upper_hsv]

    return default_dict