#!/usr/bin/python
#coding:utf-8   #强制使用utf-8编码格式
import time
import sys
import os
import itchat

itchat.auto_login(hotReload=True)   #热启动你的微信

room = itchat.search_friends(name=u'friendname')  #这里输入你好友的名字或备注。
print(room)
userName = room[0]['UserName']

dir_name =  "pic/" + time.strftime('%Y-%m-%d',time.localtime(time.time()))
os.system("mkdir -p %s" % (dir_name));

for num in range(1, 1000000):
    print num
    image_name = dir_name + "/" + time.strftime('%H-%M-%S',time.localtime(time.time())) + ".jpg"
    msg = "Home Time:" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #树莓派摄像头拍照
    os.system("raspistill -t 2000 -o %s -q 5" % (image_name));
    #给自己发图片
    itchat.send(msg)
    itchat.send_image(image_name)
    #朋友发图片
    itchat.send(msg,userName)
    itchat.send_image(image_name, userName)
    #图片发太频繁容易发失败，所有添加时间间隔
    time.sleep(60)
    print("send success")
