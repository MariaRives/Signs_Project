# Generated by Django 4.2.6 on 2023-12-05 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0011_preference"),
    ]

    operations = [
        migrations.CreateModel(
            name="Importance",
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
                (
                    "importance",
                    models.IntegerField(
                        choices=[
                            (1, "One"),
                            (2, "Two"),
                            (3, "Three"),
                            (4, "Four"),
                            (5, "Five"),
                            (6, "Six"),
                            (7, "Seven"),
                            (8, "Eight"),
                            (9, "Nine"),
                            (10, "Ten"),
                        ],
                        default=5,
                    ),
                ),
                (
                    "sign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Importances",
                        to="polls.sign",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Importances",
                        to="polls.subject",
                    ),
                ),
            ],
        ),
    ]