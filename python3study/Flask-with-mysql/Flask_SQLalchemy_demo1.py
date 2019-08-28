# coding=utf-8
# pip install flask-sqlalchemy

# pip install flask-mysqldb

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:abc@123@127.0.0.1:3306/flask_sql_demo'
# 跟踪数据库的修改--->不建议开启，首先消耗性能，其次未来的版本中会删除
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 两张表
# 角色（管理员、普通用户
# 用户（角色ID）

# 数据库的模型，需要继承db.Model


class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'

    # 定义字段
    # db.Column表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    #配置关联
    #表示和User模型发生了关联，增加了user属性
    user=db.relationship('User',backref='role')
    #repr()方法显示一个可读字符串
    def __repr__(self):
        return '<Role:%s %s>' % (self.name,self.id)




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email=db.Column(db.String(32),unique=True)
    password=db.Column(db.String(32))
    # db.ForeignKey('rolrs.id'),表明是外健
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #User希望有role属性，但是这个属性的定义，需要在另外一个模型中型定义

    def __repr__(self):
        return '<User: %s %s %s %s>' % (self.name,self.id,self.email,self.password)
        



#通过session进行数据库的添加删改
#db.session.add(role)
#db.session.commit()
#
#user=User(name='yangchao',role_id=role.id)
#db.session.add(user)
#db.session.commit()
#
#user.name='python'
#db.session.commit()
#db.seesion.delete(user)
#db.session.commit()


@app.route('/')
def index1():
    return 'Hello flask!'


if __name__ == '__main__':
    #删除表
    db.drop_all()
    #创建表
    db.create_all()
    app.run(host='0.0.0.0')
