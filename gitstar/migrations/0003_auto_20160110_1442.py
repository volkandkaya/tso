# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gitstar', '0002_auto_20160110_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stargazer',
            old_name='comapny',
            new_name='company',
        ),
    ]
