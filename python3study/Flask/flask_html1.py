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

#使用同一个视图函数，来显示不同用户的订单信息
#<>来定义路由的参数 <>内需要起个名字
@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
#需要在视图函数的（）内填如参数名，那么后面的代码才能去使用
    print (type(order_id))

    #有时候，需要对路由做访问优化，订单ID应该是INT类型
    return 'order_id %s' % order_id


#4、启动程序
if __name__ == '__main__':
    app.run(host='0.0.0.0')