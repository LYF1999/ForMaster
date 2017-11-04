# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ActionSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, unique=True)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='action.ActionSeries'),
        ),
    ]