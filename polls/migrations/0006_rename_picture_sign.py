# Generated by Django 4.2.6 on 2023-12-02 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0005_picture_imgurl"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Picture",
            new_name="Sign",
        ),
    ]
