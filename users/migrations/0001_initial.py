# Generated by Django 4.0.2 on 2022-02-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('content', models.CharField(max_length=255, verbose_name='内容')),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(max_length=255, verbose_name='发起人')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('openid', models.CharField(max_length=255, verbose_name='openid')),
                ('userName', models.CharField(max_length=255, verbose_name='用户名')),
                ('avatarUrl', models.CharField(max_length=255, verbose_name='头像')),
            ],
        ),
    ]