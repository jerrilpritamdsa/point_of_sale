# Generated by Django 3.0.8 on 2020-08-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0009_auto_20200805_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ordered_times',
            field=models.IntegerField(default=0),
        ),
    ]
