# Generated by Django 3.1.4 on 2020-12-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20201213_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='enddate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='startdate',
            field=models.DateField(null=True),
        ),
    ]
