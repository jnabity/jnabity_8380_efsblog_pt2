# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 03:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_mutualfund'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mutualfund',
            old_name='purchase_new_asset_value',
            new_name='purchase_net_asset_value',
        ),
    ]
