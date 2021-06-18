import re
import uuid
import requests
import os
import numpy
import imghdr
from PIL import Image


# 获取百度图片下载图片
def download_image(key_word, save_name, download_max):
    download_sum = 0
    str_gsm = '80'
    # 把每个类别的图片存放在单独一个文件夹中
    save_path = 'images' + '/' + save_name
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    while download_sum < download_max:
        # 下载次数超过指定值就停止下载
        if download_sum >= download_max:
            break
        str_pn = str(download_sum)
        # 定义百度图片的路径
        # url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&' \
        #       'word=' + key_word + '&pn=' + str_pn + '&gsm=' + str_gsm + '&ct=&ic=0&lm=-1&width=0&height=0'
        url = "http://www.shihuo.cn/freestyle/list?page_size=60&scene=%E9%9E%8B%E7%B1%BB&sort=hot"
        print('正在下载 %s 的第 %d 张图片.....' % (key_word, download_sum))
        # try:
        # 获取当前页面的源码
        # result = requests.get(url, timeout=30).text
        result = """
        <a href="//www.shihuo.cn/freestyle/list?page_size=60&amp;scene=%E9%9E%8B%E7%B1%BB&amp;sort=hot&amp;price=0-100#qk=shaixuan">0-100</a>
<a href="//www.shihuo.cn/freestyle/list?page_size=60&amp;scene=%E9%9E%8B%E7%B1%BB&amp;sort=hot&amp;price=100-300#qk=shaixuan">100-300</a>
<a href="//www.shihuo.cn/freestyle/list?page_size=60&amp;scene=%E9%9E%8B%E7%B1%BB&amp;sort=hot&amp;price=300-500#qk=shaixuan">300-500</a>
<a href="//www.shihuo.cn/freestyle/list?page_size=60&amp;scene=%E9%9E%8B%E7%B1%BB&amp;sort=hot&amp;price=500-1000#qk=shaixuan">500-1000</a>
<a href="//www.shihuo.cn/freestyle/list?page_size=60&amp;scene=%E9%9E%8B%E7%B1%BB&amp;sort=hot&amp;price=1000-10000#qk=shaixuan">1000-10000</a>
<a href="//www.shihuo.cn/freestyle/list?page_size=60&amp;scene=%E9%9E%8B%E7%B1%BB&amp;sort=hot&amp;price=10000%E4%BB%A5%E4%B8%8A#qk=shaixuan">10000以上</a>
</span>
</li>
</ul>
</div>
<div class="select-bar">
<ul>
<li class="sub">
<a href="//www.shihuo.cn/freestyle/list?page_size=60&amp;scene=%E9%9E%8B%E7%B1%BB&sort=hot"  class="cur">人气</a>
<a href="//www.shihuo.cn/freestyle/list?page_size=60&amp;scene=%E9%9E%8B%E7%B1%BB&sort=price_d">价格<span class="sort"></span></a>
</li>
</ul>
<div class="filter-activity">
共<span>9596</span>件商品</div>
</div>
<ul id="js_hover" class="list-ul get_json clearfix">
<li data-styleId="7070295" data-goodsId="824064">
<div class="imgs-area">
<div class="img">
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/824064.html#qk=list">
<img src="http://shihuo.hupucdn.com/def/20201215/0f8f6496b39d93019bc73e5f983735541608011452.jpg" alt="森马 马丁靴 610331401" >
</a>
</div>
</div>
<div class="style">
<p>1种配色</p>
</div>
<div class="title">
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/824064.html#qk=list">森马 马丁靴 610331401</a>
</div>
<div class="price">
<div class="tk">暂无购买链接</div></div>
<div class="style-box">
<div class="img-box clearfix"></div>
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/824064.html#qk=list">
<div class="title">
森马 马丁靴 610331401
</div>
<div class="price">
<div class="tk">暂无购买链接</div></div>
</a>
</div>
</li>
<li data-styleId="1675172" data-goodsId="538613">
<div class="imgs-area">
<div class="img">
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/538613.html#qk=list">
<img src="http://shihuo.hupucdn.com/def/20200304/f29310066261829293c06d734c913f261583313690.jpg" alt="回力 时尚潮流休闲板鞋 WXY-A928" >
</a>
</div>
</div>
<div class="style">
<p>3种配色</p>
</div>
<div class="title">
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/538613.html#qk=list">回力 时尚潮流休闲板鞋 WXY-A928</a>
</div>
<div class="price">
<span><b>¥89</b>起</span><div class="tk">2条购买链接</div></div>
<div class="style-box">
<div class="img-box clearfix"></div>
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/538613.html#qk=list">
<div class="title">
回力 时尚潮流休闲板鞋 WXY-A928
</div>
<div class="price">
<span><b>¥89</b>起</span><div class="tk">2条购买链接</div></div>
</a>
</div>
</li>
<li data-styleId="6585837" data-goodsId="778920">
<div class="imgs-area">
<div class="img">
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/778920.html#qk=list">
<img src="http://shihuo.hupucdn.com/def/20201115/5082227159b74322550bd85bc7d6e8321605402802.jpg" alt="361° 经典休闲系列 休闲鞋 672046611" >
</a>
</div>
</div>
<div class="style">
<p>3种配色</p>
</div>
<div class="title">
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/778920.html#qk=list">361° 经典休闲系列 休闲鞋 672046611</a>
</div>
<div class="price">
<span><b>¥149</b>起</span><div class="tk">3条购买链接</div></div>
<div class="style-box">
<div class="img-box clearfix"></div>
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/778920.html#qk=list">
<div class="title">
361° 经典休闲系列 休闲鞋 672046611
</div>
<div class="price">
<span><b>¥149</b>起</span><div class="tk">3条购买链接</div></div>
</a>
</div>
</li>
<li data-styleId="1222501" data-goodsId="423829">
<div class="imgs-area">
<div class="img">
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/423829.html#qk=list">
<img src="http://shihuo.hupucdn.com/trade/reposition/2020-12-03/22545da44d62efac20bb1495d5770ece.png" alt="回力 百搭休闲板鞋 3659N" >
</a>
</div>
</div>
<div class="style">
<p>4种配色</p>
</div>
<div class="title">
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/423829.html#qk=list">回力 百搭休闲板鞋 3659N</a>
</div>
<div class="price">
<div class="tk">暂无购买链接</div></div>
<div class="style-box">
<div class="img-box clearfix"></div>
<a class="link" target="_blank" href="//www.shihuo.cn/sports/detail/423829.html#qk=list">
<div class="title">
回力 百搭休闲板鞋 3659N
</div>
<div class="price">"""

        # print(result)
        # 获取当前页面的图片URL
        # img_urls = re.findall('"objURL":"(.*?)",', result, re.S)
        # img_urls = re.findall("http://shihuo.hupucdn.com/",result,re.S)
        # string = r"^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$"
        # string = r"^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$"
        string = '"objURL":"(.*?)",'
        string = '<img src="(.*?)"'
        # string = "([hH][tT]{2}[pP]://|[hH][tT]{2}[pP][sS]://|[wW]{3}.|[wW][aA][pP].|[fF][tT][pP].|[fF][iI][lL][eE].)[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]"
        img_urls = re.findall(string,result,  re.S)
        # pattern = re.compile(r'http://shihuo.hupucdn.com/[def]*/\w*/[\w\W\d\D]*(.jpg)')

        # input()
        # print(pattern.search(result))
        # print(img_urls)
        # img_urls = pattern.search(result)
        print(img_urls)
        input()
        if len(img_urls) < 1:
            break
        # 把这些图片URL一个个下载
        for img_url in img_urls:
            # 获取图片内容
            img = requests.get(img_url, timeout=30)
            img_name = save_path + '/' + str(uuid.uuid1()) + '.jpg'
            # 保存图片
            with open(img_name, 'wb') as f:
                f.write(img.content)
            download_sum += 1
            if download_sum >= download_max:
                break
        # except Exception as e:
        #     print('【错误】当前图片无法下载，%s' % e)
        #     download_sum += 1
        #     continue
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
    key_words = {'老人摔倒': 'fall'}
    # 每个类别下载一千个
    max_sum = 500
    for key_word in key_words:
        save_name = key_words[key_word]
        download_image(key_word, save_name, max_sum)

    # 删除错误图片
    delete_error_image('images/')
