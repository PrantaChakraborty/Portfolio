# Generated by Django 3.1 on 2020-08-06 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200806_0758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('gpa', models.FloatField(max_length=5)),
                ('start_date', models.DateField(default=datetime.date(2020, 8, 6))),
                ('finish_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]