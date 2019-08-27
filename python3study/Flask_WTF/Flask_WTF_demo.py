# coding=utf-8
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
# 目的：实现一个简单的登陆逻辑处理
# 1、路由需要有GET和POST两种请求方式 --》需要判断请求方式
# 2、获取请求的参数
# 3、判断参数是欧填写以及密码是否相同
# 4、如果判断都没有问题，就返回success
def index1():
    # request:请求对象--》获取方式、数据
    # 1、判断获取请求方式
    if request.method == 'POST':
        # 2、获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('password2')
        print(password)

        # 判断参数是否填写，密码是否相同
        if not all([username, password, confirm_password]):
            print('参数不完整')

        elif password != confirm_password:
            print('密码不一致')
        else:
            return 'success'
    return render_template('index1.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
