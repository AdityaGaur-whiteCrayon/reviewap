# Generated by Django 3.2.5 on 2021-07-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_auto_20210723_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
