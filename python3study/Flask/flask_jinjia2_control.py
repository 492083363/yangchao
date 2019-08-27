from flask import Flask, render_template


app = Flask(__name__)

# 1.如何返回一个网页（模板）
# 2.如何给模板填充数据


@app.route('/')
def index():
    # 传入网址
    url_str = 'www.hbct.work'
    my_list = [1, 3, 5, 7, 9]
    # 通常，模板中使用的变量名和要传递的数据变量名保持一致
    my_dict = {
        'name': 'tree new bee',
        'code': 'holy high'
    }
    my_int=38
    
    return render_template('jinjia2_control.html',
                                         url_str=url_str, 
                                         my_list=my_list, 
                                         my_dict=my_dict,
                                         my_int=my_int
                                         )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
