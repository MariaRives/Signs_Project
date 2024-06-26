# Generated by Django 4.2.6 on 2023-12-02 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0006_rename_picture_sign"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reaction_Time",
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
                ("reactionTime", models.FloatField()),
                (
                    "sign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ReactionTimes",
                        to="polls.sign",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ReactionTimes",
                        to="polls.subject",
                    ),
                ),
            ],
        ),
    ]
