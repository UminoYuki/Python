# 获取本地的当天日期的数据库，并将其上传到云端

import pymysql, json
from datetime import date, datetime


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
db_could = pymysql.connect(host="120.78.72.189",user="root",password="123456",database="simply",charset='utf8mb4')

# 使用cursor（）方法创建一个游标对象cursor
cursor = db.cursor()
cursor_could = db_could.cursor()

data = {'Temperature':1 ,'Humidity':1,'ts':1}
# 获取当天日期
today = date.today()

sql="SELECT * FROM temp_humi_data WHERE to_days(ts) = to_days(now())"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for x in results:  
        data['Temperature'] = x[1]
        data['Humidity'] = x[2]
        # s = x[3]
        # print(s)
        # print(type(s))
        data['ts'] = x[3].strftime("%Y-%m-%d %H:%M:%S")
        print(data)

        
        sql_could = "INSERT INTO Temp_Humi_Data (Temperature,Humidity,ts)  VALUES ('%s','%s','%s');" %(data['Temperature'],data['Humidity'],data['ts'])
        cursor_could.execute(sql_could)
        db_could.commit()
        print("数据库保存成功！")
except:
    print("Error: unable to fetch data")

db.close()
db_could.close()











# # 重新构造json类，遇到日期特殊处理，其余的用内置
# class ComplexEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, date):
#             return obj.strftime('%Y-%m-%d')
#         else:
#             return json.JSONEncoder.default(self, obj)


# def get_result():
#     # 需要执行的sql语句
#     sql = "sql"
#     cursor.execute(sql) 
#     data = cursor.fetchall()  
#     cols = cursor.description 
#     res = format_data(cols, data)
#     cursor.close()
#     db.close()  
#     # json.dumps(): 对数据进行编码，转成json格式
#     data_json = json.dumps(res, cls=ComplexEncoder,
#                            indent=1) 
#     # 写入文档datajson
#     with open('datajson', 'w')as file:
#         file.write(data_json)


# # 数据格式化 cols字段名，data结果集
# def format_data(cols, data):
#     # 字段数组 形式['id', 'name', 'password']
#     col = []  # 创建一个空列表以存放列名
#     for i in cols:
#         col.append(i[0])
#     # 返回的数组集合 形式[{'id': 1, 'name': 'admin', 'password': '123456'}]
#     res = []
#     for iter in data:
#         line_data = {}
#         for index in range(0, len(col)):
#             line_data[col[index]] = iter[index]
#         res.append(line_data)
#     return res

# def main():
#     get_result()
#     print("ssss")

# if __name__ == '__main__':
#     main()