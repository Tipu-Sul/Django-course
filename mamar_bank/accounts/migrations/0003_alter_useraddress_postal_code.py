# Generated by Django 4.2.7 on 2023-12-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_birthday_userbankaccount_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]
