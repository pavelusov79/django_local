# Generated by Django 3.0.4 on 2020-10-16 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_auto_20201011_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 18, 9, 24, 34, 779056)),
        ),
    ]
