# Generated by Django 3.0.4 on 2020-09-11 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20200903_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 13, 6, 19, 17, 204352)),
        ),
    ]
