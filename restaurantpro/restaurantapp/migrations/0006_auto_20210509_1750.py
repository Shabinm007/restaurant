# Generated by Django 3.2.2 on 2021-05-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0005_rename_room_id_booking_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='Name',
            new_name='Status_Name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='Code',
        ),
        migrations.AlterField(
            model_name='rooms',
            name='Offer_Price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Offer_Price'),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='Vat_Amt',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Vat_Amt'),
        ),
    ]
