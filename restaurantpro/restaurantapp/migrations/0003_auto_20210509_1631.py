# Generated by Django 3.2.2 on 2021-05-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0002_booking_room_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advance_payment',
            old_name='Name',
            new_name='Party_Name',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='Name',
            new_name='Party_Name',
        ),
        migrations.AlterField(
            model_name='booking',
            name='Code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Code',
            field=models.CharField(max_length=100),
        ),
    ]
