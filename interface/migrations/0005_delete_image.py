# Generated by Django 4.1.4 on 2023-01-07 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("interface", "0004_rename_hotel_image"),
    ]

    operations = [
        migrations.DeleteModel(name="Image",),
    ]
