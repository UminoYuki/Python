# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*
# 订阅消息存入数据库
# 数据库 pidata
# 表 temp_humi_data
# 温度，湿度，时间戳
# 接收数据到mysql中
# 每天上午11点将数据同步至云服务器中

import paho.mqtt.client as mqtt
from datetime import date, datetime
import json
import pymysql
import time

# 初始化程序
#######################################################################################################

# mydb = pymysql.connect(
    
#     host="localhost", #默认用主机名
#     port=3306,
#     user="root",  #默认用户名
#     password="123456",   #mysql密码
#     database='pidata', #库名
#     charset='utf8mb4'   #编码方式
# )
 
# print(mydb)
# #创建表
# # # 获取游标 承载结果
# mycursor = mydb.cursor()
 
# mycursor.execute("create table temp_humi_data_test(id INT(11), Place CHAR(4), Temperature FLOAT(4),Humidity FLOAT(4),ts timestamp)")

# # 关闭数据库连接
# mydb.close()

########################################################################################################

#########################

# mqtt连接基本参数
# 服务器地址
# host = '120.78.72.189'
# # 通信端口 默认端口1883
# port = 1883
# username = 'admin'
# password = 'public'
# 发布主题名称
topic_syn = 'wnj'
# 服务器地址
host = '120.78.72.189'
# 通信端口 默认端口1883
port = 1883

username = 'admin'
password = 'public'

# 订阅主题名
topic = 'topi'

# 获取时间戳
def gettime():
    time_now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return time_now

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
    global dddd
    # 打印订阅消息主题
    # print("topic", msg.topic)
    # 打印消息数据
    jsondata=json.loads(msg.payload)
    print("msg payload", jsondata) # 打印收到的数据
    sqlsave(jsondata) # 保存至数据库

def main():
    
    client = mqtt.Client()
    # 注册事件
    client.on_connect = on_connect # 链接mqtt服务器
    client.on_message = on_message # 接收到数据后的处理操作
    # 设置账号密码（如果需要的话）
    client.username_pw_set(username, password=password)
    # 连接到服务器
    client.connect(host, port=port, keepalive=60)
    # 守护连接状态

    client.loop_forever()

#MySQL保存
def sqlsave(jsonData):
      # 打开数据库连接
    db = pymysql.connect(host="localhost",user="root",password="123456",database="springboot-vue",charset='utf8mb4')
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 插入语句
    try:
        sql = "INSERT INTO data(place,temperature,humidity,ts)  VALUES ('%s','%s','%s','%s');" %(jsonData['Place'],jsonData['Temperature'],jsonData['Humidity'],gettime())
        cursor.execute(sql)
        db.commit()
        print("数据库保存成功！")
    except:
        print("保存失败")
        pass

    db.close()


if __name__ == '__main__':

    main()




