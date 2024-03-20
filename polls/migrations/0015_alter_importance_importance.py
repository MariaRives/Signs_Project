# Generated by Django 4.2.6 on 2024-01-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0014_rename_sign_signal_rename_sign_importance_signal_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="importance",
            name="importance",
            field=models.IntegerField(
                choices=[
                    (0, "Zero"),
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
    ]
