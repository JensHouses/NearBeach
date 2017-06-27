# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 07:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0002_initialise_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation_customers_documents',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='organisation_customers_documents',
            name='organisation_id',
        ),
        migrations.RemoveField(
            model_name='organisation_customers_documents',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='organisation_customers_documents',
        ),
    ]
