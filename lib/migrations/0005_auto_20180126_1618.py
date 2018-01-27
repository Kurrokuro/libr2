# Generated by Django 2.0rc1 on 2018-01-26 10:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0004_book_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 26, 10, 18, 38, 972512, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='book',
            name='unlike',
            field=models.IntegerField(default=0),
        ),
    ]
