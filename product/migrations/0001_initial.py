# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2020-12-07 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(default='', max_length=50, verbose_name='产品名称')),
                ('p_price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='产品价格')),
                ('p_introduction', models.CharField(default='', max_length=250, verbose_name='产品介绍')),
                ('p_details', models.CharField(default='', max_length=250, verbose_name='产品详情')),
                ('p_picture', models.ImageField(upload_to='Stage/Project/CMKJ_website/static/images', verbose_name='产品图片')),
            ],
            options={
                'verbose_name_plural': '产品表',
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_category_name', models.CharField(default='', max_length=50, verbose_name='分类名称')),
                ('c_category_alias', models.CharField(default='', max_length=50, verbose_name='分类别名')),
                ('c_parent_catalog', models.CharField(default='', max_length=50, verbose_name='父级分类目录')),
                ('c_category_description', models.CharField(default='', max_length=250, verbose_name='分类描述')),
                ('c_SEO_title', models.CharField(default='', max_length=50, verbose_name='SEO标题')),
                ('c_SEO_Keyword', models.CharField(default='', max_length=250, verbose_name='SEO关键字')),
                ('c_category_thumbnail', models.ImageField(upload_to='Stage/Project/CMKJ_website/static/images', verbose_name='分类缩略图')),
                ('c_PC_advertisement', models.CharField(default='', max_length=250, verbose_name='PC端广告')),
                ('c_Mobile_advertisement', models.CharField(default='', max_length=250, verbose_name='移动端广告')),
            ],
            options={
                'verbose_name_plural': '产品分类表',
                'db_table': 'ProductCategory',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='p_category_name',
            field=models.ManyToManyField(to='product.ProductCategory'),
        ),
    ]
