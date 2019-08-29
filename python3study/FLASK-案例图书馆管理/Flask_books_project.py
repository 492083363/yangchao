# coding=utf-8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# 配置数据库的地址
# 跟踪数据库的修改--->不建议开启，首先消耗性能，其次未来的版本中会删除
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:abc@123@127.0.0.1:3306/flask_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建数据库对象
db = SQLAlchemy(app)


# 1、配置数据库
# a.导入SQLAlchemy扩展
# b.创建db对象，并配置参数
# c.终端创建数据库
# 2、添加书和作者的模型
# a.模型继承db.Model
# b.__tablename__表名
# c.db.Column:字段
# d.db.relationship,关系引用

# 3、添加数据
# 4、使用模板显示数据库查询的数据
#a.查询所有的作者信息，让信息传递给模板
#b.模板中按照格式，依次for循环（作者获取数据，用的是关系引用）
# 5、使用WTF表单
# 6、实现相关的增删逻辑


# 定义书和作者模型
# 作者模型
class Author(db.Model):
    # 表名
    __tablename__ = 'authors'

    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 关系引用
    # books是给自己用的，author是给book模型使用的
    books = db.relationship('Book', backref='author')

    def _repr__(self):
        return 'Author: %s ' % (self.name)

# 书籍模型


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def _repr__(self):
        return 'Author: %s ' % (self.name, self.author_id)


@app.route('/')
def index():
    # 查询所有的作者信息，让信息传递给模板
    authors = Author.query.all()
    # 传入模板
    return render_template('books.html', authors=authors)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # 生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老杨')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我书读的少，你别骗我', author_id=au2.id)
    bk3 = Book(name='如何拿高工资', author_id=au3.id)
    bk4 = Book(name='如何征服美少女', author_id=au3.id)
    bk5 = Book(name='如何变强', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()

    app.run(host='0.0.0.0')
    
