# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2020-12-13 17:22
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_auto_20201212_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='c_details',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='案例详情'),
        ),
    ]