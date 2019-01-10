# 12306captcha
12306 captcha recognition (forward only)

# 简介
本项目是一个训练好的验证码识别（forward）服务程序
配合项目：https://github.com/testerSunshine/12306 可以实现自动抢票

# 测试环境
Python 3.6
Tensorflow 1.7.1
Flask 1.0.2

# 自动抢票功能使用
1. 安装相关环境, 运行./online_12306/servermain.py 启动验证码服务程序

2. 将GetRandCode.py 替换自动抢票程序（https://github.com/testerSunshine/12306）中的 ./inter/GetRandCode.py

3. 运行抢票程序 

# 声明
本程序只是对12306验证码识别技术研究，不准用于商业活动。
