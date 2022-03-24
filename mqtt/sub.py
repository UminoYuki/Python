# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*
# 消息订阅
# 主题：testyuki

import paho.mqtt.client as mqtt
import json

import time

def gettime():
    time1=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return time1

# 服务器地址
host = '120.78.72.189'
# 通信端口 默认端口1883
port = 1883


username = 'admin'
password = 'public'

# 订阅主题名
topic = 'testyuki'


# 连接后事件
def on_connect(client, userdata, flags, respons_code):
    if respons_code == 0:
        # 连接成功
        print('Connection Succeed!')
    else:
        # 连接失败并显示错误代码
        print('Connect Error status {0}'.format(respons_code))
    # 订阅信息
    client.subscribe(topic)


# 接收到数据后事件
def on_message(client, userdata, msg):
    # 打印订阅消息主题
    # print("topic", msg.topic)
    # 打印消息数据
    jsondata=json.loads(msg.payload)
    print("msg payload", jsondata)

def main():
    client = mqtt.Client()
    # 注册事件
    client.on_connect = on_connect
    client.on_message = on_message
    # 设置账号密码（如果需要的话）
    client.username_pw_set(username, password=password)
    # 连接到服务器
    client.connect(host, port=port, keepalive=60)
    # 守护连接状态
    client.loop_forever()


if __name__ == '__main__':
    main()




