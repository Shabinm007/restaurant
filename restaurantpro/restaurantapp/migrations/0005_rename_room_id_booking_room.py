# Generated by Django 3.2.2 on 2021-05-09 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0004_auto_20210509_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Room_ID',
            new_name='Room',
        ),
    ]