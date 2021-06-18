'''
这个文件用来搜集各种获取数据和标签的奇淫异巧
'''
import os


def get_sub_class_list(dir_list, layer=0):
    '''

    :param dir_list:
    :param layer:
    :return:
    '''
    path_list = [os.path.join(cls, img_name) for cls in dir_list for img_name in os.listdir(cls)]
    if os.path.isdir(path_list[0]):
        path_list, layer = get_sub_class_list(path_list, layer=layer + 1)
    return path_list, layer


def get_datalist_label(data_dir, label2index=None, shuffle=True):
    '''
    文件存储结构是二级的，一级为数据根目录，其下的子目录包含一个类的数据，目录名为类别名称
    :param data_dir:图片总的路径，
    :param label2index:字典，标签指向索引
    :param shuffle: 是否乱序
    :return:一个包含路径的列表，一个与路径列表等长的包含类别信息的列表,一个标签转索引的字典
    '''
    assert isinstance(label2index, dict) or label2index is None, 'label2index must be a dict or None'
    list_classes = list(map(lambda x: os.path.join(data_dir, x), os.listdir(data_dir)))
    print(list_classes)
    path_list = [os.path.join(cls, img_name) for cls in list_classes for img_name in os.listdir(cls)]
    if shuffle:
        from random import shuffle
        shuffle(path_list)
    label_list = [os.path.basename(os.path.dirname(img_path)) for img_path in path_list]
    if label2index is None:
        try:
            label2index = dict(zip(sorted(set(label_list), key=lambda x: eval(x)), list(range(len(label_list)))))
        except:
            label2index = dict(zip(sorted(set(label_list)), list(range(len(label_list)))))
        # print(label2index)
    label_index_list = [label2index[label] for label in label_list]
    return path_list, label_list, label_index_list, label2index


def walk(dir_name):
    results = []
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            results.append(os.path.join(root, file))
    return results


if __name__ == '__main__':
    path_list, label_index_list, label2index = get_datalist_label('../../trainval_data')
