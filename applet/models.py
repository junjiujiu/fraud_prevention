from django.contrib import admin
from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.AutoField(primary_key=True)
    openid = models.CharField('openid', max_length=255)
    userName = models.CharField('用户名', max_length=255, null=True)
    avatarUrl = models.CharField('头像', max_length=255, null=True)
    swindledNum = models.FloatField('被诈骗指数', null=True)


class News(models.Model):
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)
    title = models.CharField("标题", max_length=255)
    content = models.TextField("内容")
    createTime = models.DateTimeField('创建时间',  null=True, default=timezone.now)
    source = models.CharField("发起人", max_length=255)
    type = models.CharField("类型", default="1", choices=(('1', "近期新闻"), ('2', "经典案例")), max_length=1)
    img = models.CharField(max_length=255, null=True, blank=True)


class AssessMessage(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    messageInfo = models.TextField("短信内容")
    percentage = models.FloatField("是诈骗信息的概率")


class Redis(models.Model):
    id = models.AutoField(primary_key=True)
    mkey = models.CharField("标题", max_length=50)
    content = models.CharField("内容", max_length=500)
    expireTime = models.DateTimeField("过期时间")


# 添加后台django的CRUD界面
admin.site.register(User)
admin.site.register(News)
admin.site.register(AssessMessage)
