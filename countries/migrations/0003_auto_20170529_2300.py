# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20170430_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locale',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locales', to='countries.Language', verbose_name='language'),
        ),
    ]
