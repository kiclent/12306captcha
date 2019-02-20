# 12306captcha
12306 captcha recognition (forward only)

# 简介
本项目是一个基于深度学习的12306验证码本地识别程序，这是一个训练好的模型（forward）可直接部署应用
<BR>本项目配合自动抢票程序：https://github.com/testerSunshine/12306 可以实现自动抢票

# 测试环境
 - Python 3.6
 - Tensorflow 1.7.1（使用GPU加速则安装: tensorflow-gpu ）
 - Flask 1.0.2
 - numpy 1.14.3 
 - Pillow 5.1.0 

# 自动抢票功能使用
1. 安装相应环境依赖包, 运行./online_12306/servermain.py 启动验证码服务程序 (windows用户需要将里面的 ip 改为 127.0.0.1)

2. 将 GetRandCode.py 替换自动抢票程序（https://github.com/testerSunshine/12306 )中的 ./inter/GetRandCode.py  (windows 用户需要将里面的 ip 改为 127.0.0.1)

3. 运行自动抢票程序(参考原项目说明)

4. 验证码程序会将每次识别结果保存在 ./online_12306/logs 下面，识别结果文件命名格式为[timestamp_文字内容_选项1_[选项2]]，如 "20190101000000_红枣_1_3_7.png" 表示本次验证码识别到文字内容为红枣，对应图片是第1、3、7张.

#### 注意
 - 本程序在python3环境下运行， 自动抢票程序在python2环境下运行，要实现自动抢票功能需要在两个环境下分别运行（依赖包安装也要分别安装）;
 - 程序未对验证码识别结果保存数量进行限制，因此需要手动定期清理 ./online_12306/logs ，也可以将 ./online_12306/server_main.py 保存图片的语句注释掉，不保存识别结果.


# 说明
1. 测试总体的准确率在 85% 左右，识别速度 10fps (CPU only, MacBook Pro Intel Core i5)

2. online_12306/log下面保存了每次请求的验证码识别结果（这里没有对保存的图片数量进行限制，需要手动定时清理）

3. 可在./online_12306/server_main.py和GetRandCode.py中修改服务程序的端口号, windows用户可能需要将IP 0.0.0.0 改为 127.0.0.1

4. 如果需要将服务程序部署到服务器，需要修改两个项目间验证码的传输方式（GetRandCode.py程序和server_main.py），感兴趣的请自行探索

5. 有问题的话欢迎大家 Issue 或者 E-mail: kiclent@yahoo.com

6. 最后，感谢自动抢票程序送我回家， 祝大家好运 ^_^

# FAQ
Q. 登陆过程中，自动抢票程序连续出现验证码校验失败的情况
<BR>A. 这可能是自动抢票程序的Bug（详情咨询项目作者），可以通过查看验证码识别结果（./online_12306/log/）是否正确来定位问题

Q. Windows 系统出现请求失败返回 HTTP xxxx 类似的信息。
<BR>A. 把IP 0.0.0.0 换成 127.0.0.1
 
# 声明
本程序只是对12306验证码识别技术研究，不准作商业用途。
