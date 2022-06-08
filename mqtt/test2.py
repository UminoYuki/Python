# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*
# 订阅消息存入数据库
# 数据库 pidata
# 表 temp_humi_data
# 温度，湿度，时间戳
# 接收数据到mysql中
# 每天数据同步至云服务器中

import paho.mqtt.client as mqtt
from datetime import date, datetime
import json
import pymysql
import time

# 初始化程序

topic_syn = 'wnj'
# 服务器地址
host = '120.78.72.189'
# 通信端口 默认端口1883
port = 1883

username = 'admin'
password = 'public'

# 订阅主题名
topic = 'topi'

# # 打开数据库连接
# param = {
#     'host': 'localhost',
#     'port': 3306,
#     'db': 'pidata',
#     'user': 'root',
#     'password': '123456',
# }
# db = pymysql.connect(**param) #本地数据库
# cursor = db.cursor()

# data = {'Place':'1','Temperature':1 ,'Humidity':1,'ts':1}
# # 获取当天日期
# today = date.today()
# sql="select top 20 * from temp_humi_data order by pidata desc"
# sql="SELECT * FROM temp_humi_data WHERE to_days(ts) = to_days(now())"
# sql2="DELETE FROM temp_humi_data WHERE to_days(ts) = to_days(now())"

client = mqtt.Client()
client.connect(host, port, 60)

# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for x in results:  
#         data['Place'] = x[4]
#         data['Temperature'] = x[1]
#         data['Humidity'] = x[2]

#         data['ts'] = x[3].strftime("%Y-%m-%d %H:%M:%S")
#         print(data)
#         # 转换为json格式
#         jsondata = json.dumps(data)
#         # 发布数据，主题为wnj
#         client.publish(topic_syn,jsondata,2) 
print("数据同步成功！")
# except:
#     print("Error: unable to fetch data")


# db = pymysql.connect(**param) #本地数据库
# cursor = db.cursor()
# cursor.execute(sql2)
# # db.commit()
# print("成功！")
# # db.close()



#############################
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

    print("数据库保存成功！")



if __name__ == '__main__':

    main()