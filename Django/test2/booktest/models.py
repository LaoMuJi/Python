from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20) #名称
    # bprice = models.DecimalField(max_digits=10, decimal_places=2) # 价格最大位数10，小数点为2
    dpub_date = models.DateField() # 出版日期
    bread = models.IntegerField(default=0)  # 阅读量
    bcomment = models.IntegerField(default=0) # 评论量
    isDelete = models.BooleanField(default=False) # 删除标记



class HereInfo(models.Model):
    hname = models.CharField(max_length=20) # 英雄名
    hgender = models.BooleanField(default=False) # 性别
    hcomment = models.CharField(max_length=20) # 备注
    isDelete = models.BooleanField(default=False)  # 删除标记
'''
    hbook = models.ForeignKey('bookInfo') # 关联属性 一对多关系 定义在多的类中

    hbook = models.ManyToManyField('bookInfo') # 关联属性 多对多关系

    hbook = models.OneToOneField('bookInfo') # 一对一关系
'''