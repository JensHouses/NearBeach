# Generated by Django 4.0.3 on 2022-09-07 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0016_list_of_rfc_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_for_change',
            name='rfc_status_update',
            field=models.ForeignKey(default=1,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='NearBeach.list_of_rfc_status'),
            preserve_default=False,
        ),
    ]
