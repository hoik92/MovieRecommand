# Generated by Django 2.1.8 on 2019-05-16 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_score_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]