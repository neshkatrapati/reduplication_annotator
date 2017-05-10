# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reduplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=2000)),
                ('frequency', models.IntegerField(default=0)),
                ('examples', models.TextField()),
                ('types', models.CharField(max_length=2000)),
                ('change_data', models.DateTimeField(verbose_name='date changed')),
            ],
        ),
        migrations.CreateModel(
            name='ReduplicationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ReduplicationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='reduplication',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reduplications.ReduplicationCategory'),
        ),
    ]