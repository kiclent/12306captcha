#coding=utf-8
'''
12306 captcha recognition
kiclent@yahoo.com
test by: Python 3.6, Tensorflow 1.7.1

需要准备的数据有三类（共7个文件），全部放在./model_data目录下
1、模型类别映射文件，模型预测出来的是类别编号（训练时设定），用于还原模型原类别信息
2、ocr模型，用于识别验证码需要识别的关键字，共3个文件分别是 xxx.data-00000-of-00001, xxx.meta, xxx.index
3、验证码物体模型，用于识别验证码需要识别的物体，共3个文件分别是 yyy.data-00000-of-00001, yyy.meta, yyy.index
'''
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '3' # 指定GPU（如果有需要）
import numpy as np
from server_model import CaptchaModel
from time import time as tc
import time
import shutil

# 读取类别编号映射类别文件，将模型识别出来的编号还原为类别
def read_classes(classes_file):
    with open(classes_file, mode='r', encoding='utf-8') as fp:
        classes = [ c.strip() for c in fp.readlines()]
    return np.array(classes)

# 模型加载数据路径
ocr_model_meta = './model_data/ocr.ckpt-1108000.meta'
ocr_model_para = './model_data/ocr.ckpt-1108000' # 需要注意, 模型参数文件后缀 ".data-00000-of-00001" 不需要写入路径

cap_model_meta = './model_data/densenet_121.ckpt-145000.meta'
cap_model_para = './model_data/densenet_121.ckpt-145000'

classes_path = './model_data/12306_classes.txt'
classes = read_classes(classes_path)

logdir = './logs'
if not os.path.exists(logdir):
    os.makedirs(logdir)

# 加载模型
model = CaptchaModel(ocr_model_meta=ocr_model_meta,
                     ocr_model_para=ocr_model_para,
                     cap_model_meta=cap_model_meta,
                     cap_model_para=cap_model_para)

# ============ 调用示例 ============
# 建议加上日志系统，把识别的图片、识别结果保存， 方便后面问题的排查以及对验证码产生的规律进行统计分析
from flask import request, Flask
import json

app = Flask(__name__)
@app.route("/frame", methods=['POST', 'GET'])
def get_frame():
    tic = tc()
    print('----------------------------------------------------------------')
    log_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print(log_time)
    res = request.json
    print(request.query_string)
    img_path = res['imgPath']
    print(img_path)
    word_ind, objs_ind = model.predict(img_path)
    Result={'Result':[]}
    for i, ind in enumerate(objs_ind):
        if ind == word_ind[0]:
            Result['Result'].append(i+1)
    if Result['Result'].__len__() <= 0:
        Result['Result'].append(np.random.randint(1, 9))
    print(classes[word_ind[0]], Result['Result'])
    pic = log_time.replace(' ', '').replace('-', '').replace(':', '') + '_' +classes[word_ind[0]] + '_' + '_'.join([str(v) for v in Result['Result']]) + '.png'
    print(pic)
    shutil.copyfile(img_path, os.path.join(logdir, pic))

    print('fetch time: {:.5f} s.'.format(tc() - tic))
    print('----------------------------------------------------------------\n')
    return json.dumps(Result)


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)  # 端口为8080

'''
测试
curl -H "Content-Type:application/json" -X POST -d '{"imgPath":"/Users/phoenix/program/12306captcha/data/12306/2.jpg"}' http://0.0.0.0:8080/frame
'''
