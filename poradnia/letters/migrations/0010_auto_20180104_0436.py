# Generated by Django 1.11.8 on 2018-01-04 03:36
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [("letters", "0009_auto_20160409_2334")]

    operations = [
        migrations.AlterField(
            model_name="letter",
            name="accept",
            field=model_utils.fields.MonitorField(
                default=django.utils.timezone.now,
                monitor="status",
                verbose_name="Accepted on",
                when={"done"},
            ),
        ),
        migrations.AlterField(
            model_name="letter",
            name="eml",
            field=models.FileField(
                help_text="Original full content of message",
                null=True,
                upload_to="messages",
                verbose_name="Raw message contents",
            ),
        ),
        migrations.AlterField(
            model_name="letter",
            name="genre",
            field=models.CharField(
                choices=[("mail", "mail"), ("comment", "comment")],
                default="comment",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="letter",
            name="status",
            field=model_utils.fields.StatusField(
                choices=[(0, "dummy")],
                db_index=True,
                default="staff",
                max_length=100,
                no_check_for_status=True,
            ),
        ),
        migrations.AlterField(
            model_name="letter",
            name="status_changed",
            field=model_utils.fields.MonitorField(
                default=django.utils.timezone.now, monitor="status"
            ),
        ),
    ]
