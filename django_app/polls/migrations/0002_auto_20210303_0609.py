# Generated by Django 3.1.7 on 2021-03-03 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 11, 9, 38, 232040), verbose_name='date published'),
        ),
    ]
