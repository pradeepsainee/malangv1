# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 11:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songplay', '0003_voterecord'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='voterecord',
            unique_together=set([('user', 'request')]),
        ),
    ]
