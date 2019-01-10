# 12306captcha
12306 captcha recognition (forward only)

# 简介
本项目是一个训练好的验证码识别（forward）服务程序
配合项目：https://github.com/testerSunshine/12306 可以实现自动抢票

# 测试环境
1. Python 3.6
2. Tensorflow 1.7.1
3. Flask 1.0.2
4. opencv-python 3.4.2.17 

# 自动抢票功能使用
1. 安装相关环境, 运行./online_12306/servermain.py 启动验证码服务程序

2. 将GetRandCode.py 替换自动抢票程序（https://github.com/testerSunshine/12306 )中的 ./inter/GetRandCode.py

<<<<<<< HEAD
3. 运行自动抢票程序
=======
3. 运行抢票程序 
>>>>>>> 44d43f34e20360c1f67b20d8665a5903571413e9

 注意：本程序运行在python3环境下， 自动抢票程序运行python2环境，因此安装环境和运行程序都需要格外注意


# 说明
1. 测试总体的准确率在75% - 85% 之间，识别速度 10fps (CPU only, MacBook Pro Intel Core i5)
<<<<<<< HEAD
2. online_12306/log下面保存了每次请求的验证码识别结果（这里没有对保存的图片数量进行限制，需要手动定时清理）
3. 可在server_main.py中修改服务程序的端口号,windows用户可能需要将IP 0.0.0.0 改为 127.0.0.1
4. 如果需要将服务程序部署到服务器，需要修改两个项目间验证码的传输方式（GetRandCode.py程序和server_main.py），感兴趣的请自行探索
5. 有问题的话欢迎大家 Issue 或者 E-mail: kiclent@yahoo.com
6. 最后，感谢自动抢票程序送我回家， 祝大家好运 ^_^

# FAQ
Q. 登陆过程中，自动抢票程序连续出现验证码校验失败的情况
<BR>A. 这可能是自动抢票程序的Bug（详情咨询项目作者），可以通过查看验证码识别结果的是否正确来定位问题（./online_12306/log/）

Q. Windows 系统出现请求失败返回HTTP xxxx 信息。
# 声明
本程序只是对12306验证码识别技术研究，不准作商业用途。
=======
2. online/log下面保存了每次请求的验证码识别结果
3. 可在server_main.py中修改服务程序的端口号
4. 如果需要将服务程序部署到服务器，需要修改两个项目间验证码的传输方式（GetRandCode.py程序和server_main.py），感兴趣的请自行探索
5. 有问题的话欢迎大家 Issue 或者 E-mail: kiclent@yahoo.com
6. 最后，感谢自动抢票程序作者送我回家， 祝大家好运 ^_^

# A&Q
Q. 登陆过程中，自动抢票程序连续出现验证码校验失败的情况
A. 这可能是自动抢票程序的Bug（详情咨询项目作者），可以通过查看验证码识别结果的是否正确（./online_12306/log/）

# 声明
本程序只是对12306验证码识别技术研究，不准作商业用途。
>>>>>>> 44d43f34e20360c1f67b20d8665a5903571413e9
