# Generated by Django 3.0.8 on 2020-07-28 16:10

from django.db import migrations, models
import django.db.models.deletion
import pos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('identity', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(null=True, upload_to=pos.models.customer_photo_directory)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('success', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='ordername',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Product'),
        ),
    ]
