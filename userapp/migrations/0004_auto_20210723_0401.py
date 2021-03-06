# Generated by Django 3.2.5 on 2021-07-22 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_auto_20210723_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='company',
        ),
        migrations.AddField(
            model_name='review',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userapp.company'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userapp.ratings'),
            preserve_default=False,
        ),
    ]
