# Generated by Django 2.1.8 on 2019-05-16 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20190516_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='user',
        ),
    ]