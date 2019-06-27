# Generated by Django 2.1.5 on 2019-03-11 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190308_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='消息')),
                ('group_name', models.TextField(verbose_name='群组名字')),
                ('status', models.BooleanField(default=False, verbose_name='任务状态')),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 3, 11, 3, 20, 42, 801088), verbose_name='任务添加时间')),
            ],
        ),
        migrations.AddField(
            model_name='groups_name',
            name='group_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='群唯一id'),
        ),
        migrations.AddField(
            model_name='groups_name',
            name='owner',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='群主'),
        ),
        migrations.AddField(
            model_name='groups_name',
            name='users_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='人数'),
        ),
    ]