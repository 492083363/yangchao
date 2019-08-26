from flask import Flask, render_template


app = Flask(__name__)

# 1.如何返回一个网页（模板）
# 2.如何给模板填充数据


@app.route('/')
def index():
    #传入网址
    url_str = 'www.hbct.work'
    return render_template('index2.html',url_str=url_str)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
