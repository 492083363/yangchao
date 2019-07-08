from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)


# Create your models here.

class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name
 
class Tag(models.Model):
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

