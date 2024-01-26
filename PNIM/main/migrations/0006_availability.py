# Generated by Django 4.1.7 on 2023-04-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_doctor_rating"),
    ]

    operations = [
        migrations.CreateModel(
            name="Availability",
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
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("d_id", models.ManyToManyField(to="main.doctor")),
            ],
            options={
                "verbose_name_plural": "Availability",
            },
        ),
    ]
