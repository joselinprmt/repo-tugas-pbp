# Generated by Django 4.1 on 2022-09-28 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mywatchlist',
            name='description',
        ),
    ]
