# Generated by Django 2.1.7 on 2019-03-22 00:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190307_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 3, 21, 21, 23, 27, 716142)),
        ),
    ]
