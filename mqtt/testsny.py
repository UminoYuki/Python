# 获取本地的当天日期的数据库，并将其上传到云端

import pymysql, json
from datetime import date, datetime
import paho.mqtt.client as mqtt
import schedule
import time

# mqtt连接基本参数
# 服务器地址
host = '120.78.72.189'
# 通信端口 默认端口1883
port = 1883
username = 'admin'
password = 'public'
# 发布主题名称
topic = 'wnj'

# 打开数据库连接
param = {
    'host': 'localhost',
    'port': 3306,
    'db': 'pidata',
    'user': 'root',
    'password': '123456',
}
db = pymysql.connect(**param) #本地数据库
# db = pymysql.connect(host="localhost",user="root",password="123456",database="pidata",charset='utf8mb4')
# 云端数据库
# db_could = pymysql.connect(host="120.78.72.189",user="root",password="123456",database="simply",charset='utf8mb4')

# 使用cursor（）方法创建一个游标对象cursor
cursor = db.cursor()
# cursor_could = db_could.cursor()

data = {'Place':1,'Temperature':1 ,'Humidity':1,'ts':1}
# 获取当天日期
today = date.today()

sql="SELECT * FROM temp_humi_data WHERE to_days(ts) = to_days(now())"

client = mqtt.Client()
client.connect(host, port, 60)

def fun():
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for x in results:  
            data['Place'] = x[4]
            data['Temperature'] = x[1]
            data['Humidity'] = x[2]
            # s = x[3]
            # print(s)
            # print(type(s))
            data['ts'] = x[3].strftime("%Y-%m-%d %H:%M:%S")
            print(data)

            # 转换为json格式
            jsondata = json.dumps(data)
            # 发布数据，主题为wnj
            client.publish(topic,jsondata,2) 
            # 守护连接状态
            # client.loop_forever()
            
            # sql_could = "INSERT INTO Temp_Humi_Data (Temperature,Humidity,ts)  VALUES ('%s','%s','%s');" %(data['Temperature'],data['Humidity'],data['ts'])
            # cursor_could.execute(sql_could)
            # db_could.commit()
            # print("数据库保存成功！")
    except:
            print("Error: unable to fetch data")

    db.close()
    # db_could.close()


schedule.every().day.at("18:15").do(fun) # 每天上午十点半同步至云服务器中
while True:
    schedule.run_pending()
    time.sleep(1)