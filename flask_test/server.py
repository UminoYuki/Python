from flask import Flask
# 第一个flask程序 hello world

app = Flask(__name__) # 程序名称
# app = Flask("my-app", static_folder="path1", template_folder="path2")
#              静态资源、模板、参考文档

# 当客户端访问/时，将响应hello_world()函数返回的内容。
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
# app.run(debug=True) 调试模式，检测到代码发生变化，会自动重启程序
# app.run(host='0.0.0.0', port=80, debug=True)
#      自定义端口号