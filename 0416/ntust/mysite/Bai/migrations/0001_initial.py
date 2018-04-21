# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-17 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('birth', models.CharField(max_length=20)),
                ('is_girl', models.BooleanField(default=False)),
            ],
        ),
    ]
