# Generated by Django 4.2.6 on 2023-12-02 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0004_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="picture",
            name="imgURL",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]