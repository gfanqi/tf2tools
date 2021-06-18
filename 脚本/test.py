import os
import pandas as pd


def result_statistic(df_result, out_path):
    '''

    统计测试结果

    :param df_result: 价格计算的结果

    :param out_path: 输出路径

    :return:

    '''

    # df_out = pd.DataFrame()

    # df_out[

    #     ['price <= 2000', '2k < price <= 2w', '2w < price <= 5w', '5w < price <= 10w',

    #      '10w < price <= 20w', '20w < price']] = None

    df_out = pd.DataFrame(columns=('', 'price <= 2000', '2k < price <= 2w', '2w < price <= 5w', '5w < price <= 10w',

                                   '10w < price <= 20w', '20w < price'))

    df_out.loc[0, ''] = '准确率'

    df_out.loc[1, ''] = '占比'

    all_num = len(df_result)

    if all_num == 0:
        # logger.error('The number of result is 0.')

        return

    all_accuracy = 0

    # 统计结果

    # 0 - 2000

    sub_result = df_result[df_result.标价 <= 2000]

    correct_num = len(sub_result[sub_result.预测价格 <= 2000])

    num = len(sub_result)

    ratio = round(num / all_num, 4)

    print('ratio: ', ratio)

    if num > 0:

        accuracy = correct_num / num

        df_out.loc[0, 'price <= 2000'] = round(accuracy, 4)

        df_out.loc[1, 'price <= 2000'] = ratio

        print(f'price <= 2000: accuracy = {correct_num} / {num} = {accuracy}')

        all_accuracy += ratio * accuracy

    else:

        df_out.loc[0, 'price <= 2000'] = '-'

        print(f'price <= 2000: accuracy = -')

    #

    # 2k - 2w

    sub_result = df_result[(2000 < df_result.标价) & (df_result.标价 <= 20000)]

    correct_num = len(sub_result[(-0.2 <= sub_result.d_value) & (sub_result.d_value <= 0.4)])

    num = len(sub_result)

    ratio = round(num / all_num, 4)

    print('ratio: ', ratio)

    if num > 0:

        accuracy = correct_num / num

        df_out.loc[0, '2k < price <= 2w'] = round(accuracy, 4)

        df_out.loc[1, '2k < price <= 2w'] = ratio

        print(f'2k < price <= 2w: accuracy = {correct_num} / {num} = {accuracy}')

        all_accuracy += ratio * accuracy

    else:

        df_out.loc[0, '2k < price <= 2w'] = '-'

        print(f'2k < price <= 2w: accuracy = -')

    # 2w - 5w

    sub_result = df_result[(20000 < df_result.标价) & (df_result.标价 <= 50000)]

    correct_num = len(sub_result[(-0.5 <= sub_result.d_value) & (sub_result.d_value <= 0.5)])

    num = len(sub_result)

    ratio = round(num / all_num, 4)

    print('ratio: ', ratio)

    if num > 0:

        accuracy = correct_num / num

        df_out.loc[0, '2w < price <= 5w'] = round(accuracy, 4)

        df_out.loc[1, '2w < price <= 5w'] = ratio

        print(f'2w < price <= 5w: accuracy = {correct_num} / {num} = {accuracy}')

        all_accuracy += ratio * accuracy

    else:

        df_out.loc[0, '2w < price <= 5w'] = '-'
        print(f'2w < price <= 5w: accuracy = -')
    # 5w - 10w
    sub_result = df_result[(50000 < df_result.标价) & (df_result.标价 <= 100000)]
    num = len(sub_result)
    # correct_num = len(sub_result[(50000 < sub_result.预测价格) & (sub_result.预测价格 <= 100000)])
    correct_num = 0
    for ir in sub_result.itertuples():
        if (50000 < ir.预测价格 <= 100000) or (-0.5 <= ir.d_value <= 0.5):
            correct_num += 1
    ratio = round(num / all_num, 4)
    print('ratio: ', ratio)
    if num > 0:
        accuracy = correct_num / num
        df_out.loc[0, '5w < price <= 10w'] = round(accuracy, 4)
        df_out.loc[1, '5w < price <= 10w'] = ratio
        print(f'5w < price <= 10w: accuracy = {correct_num} / {num} = {accuracy}')
        all_accuracy += ratio * accuracy
    else:
        df_out.loc[0, '5w < price <= 10w'] = '-'
        print(f'5w < price <= 10w: accuracy = -')
    # 10w - 20w
    sub_result = df_result[(100000 < df_result.标价) & (df_result.标价 <= 200000)]
    # correct_num = len(sub_result[(100000 < sub_result.预测价格) & (sub_result.预测价格 <= 200000)])
    correct_num = 0
    for ir in sub_result.itertuples():
        if (100000 < ir.预测价格 <= 200000) or (-0.5 <= ir.d_value <= 0.5):
            correct_num += 1
    num = len(sub_result)
    ratio = round(num / all_num, 4)
    print('ratio: ', ratio)
    if num > 0:
        accuracy = correct_num / num
        df_out.loc[0, '10w < price <= 20w'] = round(accuracy, 4)
        df_out.loc[1, '10w < price <= 20w'] = ratio
        print(f'10w < price <= 20w: accuracy = {correct_num} / {num} = {accuracy}')
        all_accuracy += ratio * accuracy
    else:
        df_out.loc[0, '10w < price <= 20w'] = '-'
        print(f'10w < price <= 20w: accuracy = -')
    # >20w
    sub_result = df_result[200000 < df_result.标价]
    # correct_num = len(sub_result[200000 < sub_result.预测价格])
    correct_num = 0
    for ir in sub_result.itertuples():
        if (200000 < ir.预测价格) or (-0.5 <= ir.d_value <= 0.5):
            correct_num += 1
    num = len(sub_result)
    ratio = round(num / all_num, 4)
    print('ratio: ', ratio)
    if num > 0:
        accuracy = correct_num / num
        df_out.loc[0, '20w < price'] = round(accuracy, 4)
        df_out.loc[1, '20w < price'] = ratio
        print(f'20w < price: accuracy = {correct_num} / {num} = {accuracy}')
        all_accuracy += ratio * accuracy
    else:
        df_out.loc[0, '20w < price'] = '-'
        print(f'20w < price: accuracy = -')
    print('all_accuracy: ', all_accuracy)

    out_path = os.path.join(out_path, 'statistic.csv')

    df_out.to_csv(out_path, encoding='GBK', index=False)
if __name__ == '__main__':
    df = pd.read_excel("result.xlsx")
    print(df)
    result_statistic(df,"./")
    pass