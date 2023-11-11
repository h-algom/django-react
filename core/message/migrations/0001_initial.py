# Generated by Django 4.2.7 on 2023-11-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("content", models.TextField()),
                ("read", models.BooleanField(default=False)),
                ("received_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
