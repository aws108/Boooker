# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0004_libros_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='sinopsis',
            field=models.TextField(default='', max_length=600),
        ),
    ]