# Generated by Django 3.2.2 on 2021-05-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0009_auto_20210512_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='Available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rooms',
            name='Reserved',
            field=models.BooleanField(default=True),
        ),
    ]