# Generated by Django 3.1.4 on 2020-12-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20201230_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='price',
            field=models.SmallIntegerField(default=0),
        ),
    ]
