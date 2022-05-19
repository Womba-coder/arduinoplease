# Generated by Django 4.0.4 on 2022-05-19 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduinoportal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='data',
        ),
        migrations.AddField(
            model_name='info',
            name='humidity',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='temperature',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]