# coding=utf-8
from PIL import Image
import os

import requests

def rk_create(imgPath):
    """
    im: 图片字节
    im_type: 题目类型
    """
    headers = {
        'Connection': 'Keep-Alive',
        'Expect': '100-continue',
        'User-Agent': 'ben',
        "Content - Type": "application/json",
    }
    # headers = {
    #     "Content - Type": "application/json",
    #     "Accept": "*/*"
    # }
    params = {
        'imgPath': imgPath,
    }
    r = requests.post('http://0.0.0.0:8080/frame', json=params)
    print(r)
    return r.json()

def getRandCode(is_auto_code, auto_code_type, result):
    """
    识别验证码
    :return: 坐标
    """
    imgPath = os.path.abspath('./tkcode.png')
    try:
        if is_auto_code:
            Result = rk_create(imgPath)
            try:
                return codexy(Ofset=",".join([ str(v) for v in Result["Result"]]), is_raw_input=False)
            except:
                print(u'打码出错')
        else:
            img = Image.open('./tkcode')
            img.show()
            return codexy()
    except Exception as e:
        print(e)


def codexy(Ofset=None, is_raw_input=True):
    """
    获取验证码
    :return: str
    """
    print('codexy')
    if is_raw_input:
        print(u"""
            *****************
            | 1 | 2 | 3 | 4 |
            *****************
            | 5 | 6 | 7 | 8 |
            *****************
            """)
        print(u"验证码分为8个，对应上面数字，例如第一和第二张，输入1, 2")
        Ofset = raw_input(u"输入对应的验证码: ")
    Ofset = Ofset.replace("，", ",")
    select = Ofset.split(',')
    post = []
    offsetsX = 0  # 选择的答案的left值,通过浏览器点击8个小图的中点得到的,这样基本没问题
    offsetsY = 0  # 选择的答案的top值
    print('++++++')
    print(select)
    for ofset in select:
        if ofset == '1':
            offsetsY = 46
            offsetsX = 42
        elif ofset == '2':
            offsetsY = 46
            offsetsX = 105
        elif ofset == '3':
            offsetsY = 45
            offsetsX = 184
        elif ofset == '4':
            offsetsY = 48
            offsetsX = 256
        elif ofset == '5':
            offsetsY = 36
            offsetsX = 117
        elif ofset == '6':
            offsetsY = 112
            offsetsX = 115
        elif ofset == '7':
            offsetsY = 114
            offsetsX = 181
        elif ofset == '8':
            offsetsY = 111
            offsetsX = 252
        else:
            pass
        post.append(offsetsX)
        post.append(offsetsY)
    randCode = str(post).replace(']', '').replace('[', '').replace("'", '').replace(' ', '')
    print(u"验证码识别坐标为{0}".format(randCode))
    return randCode
