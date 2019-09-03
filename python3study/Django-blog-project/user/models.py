from django.db import models

# Create your models here.
#Django会为模型类提供一个objects对象，它是django.db.models.manager.Manager类型，用于数据库交互。
#当定义模型类的时候没有指定管理器，则Django会为模型类一个obects的管理器
#如果在模型类中手动指定管理器后，Django不再提供默认的object管理器

#管理器是Django模型进行数据库查询操作的接口，Django应用的每个模型都至少拥有一个管理器

class USER(models.Model):
    class Meta:  # 需要定义内部类
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, null=False)
    email = models.CharField(max_length=64, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)

    def __repr__(self):
        return '<user {} {}>'.format(self.id, self.name)
        
    __str__ = __repr__
