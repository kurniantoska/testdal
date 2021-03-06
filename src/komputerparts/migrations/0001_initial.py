# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merk', models.CharField(max_length=120)),
                ('fitur', models.CharField(max_length=100)),
                ('harga', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='KomputerBuiltin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_paket', models.CharField(max_length=120)),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='komputerparts.Cpu')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merk', models.CharField(max_length=120)),
                ('tahun_pembuatan', models.CharField(max_length=4)),
                ('harga', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='komputerbuiltin',
            name='monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='komputerparts.Monitor'),
        ),
    ]
