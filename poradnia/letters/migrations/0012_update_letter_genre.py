# Generated by Django 2.2.25 on 2021-12-30 12:55

from django.db import migrations


def migrate_genre(apps, schema_editor):
    Letter = apps.get_model("letters", "Letter")
    Letter.objects.update(genre="mail")


class Migration(migrations.Migration):

    dependencies = [
        ("letters", "0011_letter_html"),
    ]

    operations = [
        migrations.RunPython(migrate_genre),
    ]