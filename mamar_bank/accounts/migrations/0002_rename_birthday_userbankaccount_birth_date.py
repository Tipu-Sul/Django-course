# Generated by Django 4.2.7 on 2023-12-24 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbankaccount',
            old_name='birthday',
            new_name='birth_date',
        ),
    ]
