# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.AddField(
            model_name='product',
            name='amount_kg',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='special_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=1),
        ),
    ]
