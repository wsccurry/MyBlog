# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-24 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('titleId', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=200)),
                ('content_other', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
    ]
