from flask import Flask, render_template
app = Flask(__name__)

#2、创建FLASK应用程序实例
#需要传输__name__，作用是为了确定资源所在的路径

#3、定义陆游及视图函数
#flask中定义路由是通过装饰器来实现的
#路由默认只支持GET，如果需要增加，需要自行指定方法
@app.route('/',methods=['GET','POST'])

def  index():
    #return 'Hello World!'
    return render_template('index.html')

#4、启动程序
if __name__ == '__main__':
    app.run(host='0.0.0.0')