# Generated by Django 4.2.7 on 2023-12-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
