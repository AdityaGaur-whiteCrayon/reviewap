# Generated by Django 3.2.5 on 2021-07-30 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_auto_20210730_0413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='other',
        ),
        migrations.AlterField(
            model_name='review',
            name='company',
            field=models.CharField(default='', max_length=50),
        ),
    ]
