# Generated by Django 3.1 on 2020-08-13 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20200809_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
