# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0003_editprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editprofile',
            old_name='pnoneno',
            new_name='phoneno',
        ),
    ]
