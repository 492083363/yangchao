from flask import Flask
#1、导入FLASK扩展

app = Flask(__name__)

#2、创建FLASK应用程序实例
#需要传输__name__，作用是为了确定资源所在的路径

#3、定义陆游及视图函数
#flask中定义路由是通过抓时期来实现的
@app.route('/')

def hello_world():
    return 'Hello World!'

#4、启动程序
if __name__ == '__main__':
    app.run(host='0.0.0.0')
