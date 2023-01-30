# Generated by Django 4.1.4 on 2023-01-07 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("interface", "0005_delete_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bgEnhance", models.BooleanField()),
                ("upsample", models.BooleanField()),
                ("fidility", models.FloatField(max_length=1)),
                ("Img", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
