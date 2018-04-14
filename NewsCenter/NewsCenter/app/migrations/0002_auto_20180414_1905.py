# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.IntegerField(choices=[(1, 'BANNED'), (2, 'GUEST'), (3, 'USER'), (4, 'MODERATOR'), (5, 'ADMINISTRATOR'), (6, 'HEAD_ADMINISTRATOR')], max_length=1),
        ),
    ]
