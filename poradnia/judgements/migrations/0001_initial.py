# Generated by Django 1.11.8 on 2018-04-15 21:08
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("events", "0010_auto_20180415_1923"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cases", "0034_auto_20180104_0436"),
    ]

    operations = [
        migrations.CreateModel(
            name="Court",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="Court")),
                (
                    "active",
                    models.BooleanField(default=True, verbose_name="Active status"),
                ),
                (
                    "parser_key",
                    models.CharField(
                        blank=True,
                        help_text="Identifier of parser",
                        max_length=10,
                        verbose_name="Parser key",
                    ),
                ),
            ],
            options={"verbose_name": "Court", "verbose_name_plural": "Courts"},
        ),
        migrations.CreateModel(
            name="CourtCase",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("signature", models.CharField(help_text="Signature", max_length=50)),
                (
                    "case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cases.Case"
                    ),
                ),
                (
                    "court",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="judgements.Court",
                        verbose_name="Court",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="courtcase_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="courtcase_modified_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Modified by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Court case",
                "verbose_name_plural": "Court cases",
            },
        ),
        migrations.CreateModel(
            name="CourtSession",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "court_case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="judgements.CourtCase",
                        verbose_name="Court case",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.Event",
                        verbose_name="Event",
                    ),
                ),
            ],
            options={
                "verbose_name": "Court session",
                "verbose_name_plural": "Court sessions",
            },
        ),
    ]
