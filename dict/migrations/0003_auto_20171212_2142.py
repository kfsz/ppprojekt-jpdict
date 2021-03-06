# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0002_auto_20171110_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='alterreading',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='word',
            name='alterword',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='word',
            name='common',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='word',
            name='reading',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='wordtl',
            name='translation',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='wordtl',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meanings', to='dict.Word'),
        ),
        migrations.AlterField(
            model_name='wordtl',
            name='word_type',
            field=models.CharField(default='', max_length=40),
        ),
    ]
