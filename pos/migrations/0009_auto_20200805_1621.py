# Generated by Django 3.0.8 on 2020-08-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0008_auto_20200805_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ordered_times',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]