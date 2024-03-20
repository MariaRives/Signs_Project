# Generated by Django 4.2.6 on 2024-01-11 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0015_alter_importance_importance"),
    ]

    operations = [
        migrations.CreateModel(
            name="Iddentify",
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
                ("guess", models.CharField(max_length=25)),
                (
                    "signal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="guesses",
                        to="polls.signal",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="guesses",
                        to="polls.subject",
                    ),
                ),
            ],
        ),
    ]
