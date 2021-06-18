import re
import time
import uuid
import requests
import os
import numpy
import imghdr
from PIL import Image


def download_image(url, key_word, save_name, download_max):
    download_sum = 0
    # 把每个类别的图片存放在单独一个文件夹中
    save_path = 'images' + '/' + save_name
    print(save_path)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    print('正在下载 %s 的第 %d 张图片.....' % (key_word, download_sum))

    # 获取当前页面的源码
    result = requests.get(url, timeout=30).text
    # 获取当前页面的图片URL
    string = '"objURL":"(.*?)",'
    string = '<img src="(.*?)"'
    img_urls = re.findall(string, result, re.S)
    print(img_urls)
    if len(img_urls) < 1:
        #
        return
    # 把这些图片URL一个个下载
    for img_url in img_urls:
        # 获取图片内容
        try:
            img = requests.get(img_url, timeout=30)
            img_name = os.path.join(save_path  ,os.path.basename(img_url))
            # 保存图片
            with open(img_name, 'wb') as f:
                f.write(img.content)
            download_sum += 1
            if download_sum >= download_max:
                break
        except Exception as e:
            print('【错误】当前图片无法下载，%s' % e)
            download_sum += 1
            # continue
    print('下载完成')

    # 删除不是JPEG或者PNG格式的图片


def delete_error_image(father_path):
    # 获取父级目录的所有文件以及文件夹
    try:
        image_dirs = os.listdir(father_path)
        for image_dir in image_dirs:
            image_dir = os.path.join(father_path, image_dir)
            # 如果是文件夹就继续获取文件夹中的图片
            if os.path.isdir(image_dir):
                images = os.listdir(image_dir)
                for image in images:
                    image = os.path.join(image_dir, image)
                    try:
                        # 获取图片的类型
                        image_type = imghdr.what(image)
                        # 如果图片格式不是JPEG同时也不是PNG就删除图片
                        if image_type is not 'jpeg' and image_type is not 'png':
                            os.remove(image)
                            print('已删除：%s' % image)
                            continue
                        # 删除灰度图
                        img = numpy.array(Image.open(image))
                        if len(img.shape) is 2:
                            os.remove(image)
                            print('已删除：%s' % image)
                    except:
                        os.remove(image)
                        print('已删除：%s' % image)
    except:
        pass


if __name__ == '__main__':
    # 定义要下载的图片中文名称和英文名称，ps：英文名称主要是为了设置文件夹名
    url = "http://www.shihuo.cn/freestyle/list?page_size=60&scene=%E9%9E%8B%E7%B1%BB&sort=hot"
    key_word = "shoes"
    save_name = "shoes"
    download_max = 100000
    # print("fs")
    download_image(url, key_word, save_name, download_max=100)

    # 删除错误图片
    # delete_error_image('images/')
