# mqtt发布测试代码
# 发布主题wnj，并到broker，保存到数据库持续化
# encoding: utf-8


import time,json
import paho.mqtt.client as mqtt

# mqtt连接基本参数
# 服务器地址
host = '120.78.72.189'
# 通信端口 默认端口1883
port = 1883
username = 'admin'
password = 'public'
# 发布主题名称
topic = 'wnj'

data = {'Temperature':1 ,'Humidity':1,'ts':1}

# 获取时间戳
def gettime():
    time_now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return time_now

def test():
    client = mqtt.Client()
    client.connect(host, port, 60)

# 数据获取
    data['Temperature'] = 12.0
    data['Humidity'] = 60.1
    data['ts'] = gettime()
# 转换为json格式
    jsondata = json.dumps(data)
# 发布数据，主题为wnj
    client.publish(topic,jsondata,2) 
# 守护连接状态
    client.loop_forever()

if __name__ == '__main__':
    test()