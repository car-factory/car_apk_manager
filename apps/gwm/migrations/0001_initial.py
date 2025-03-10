# Generated by Django 4.2.16 on 2024-12-16 12:33

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Apk",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=90,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=12)),
                ("version", models.CharField(max_length=20)),
                ("describe", models.CharField(max_length=60)),
                ("file_url", models.TextField(blank=True, max_length=300, null=True)),
                ("file_md5", models.CharField(max_length=120)),
                ("file_sha256", models.CharField(max_length=150)),
                ("is_update", models.BooleanField(default=True)),
                ("force_update", models.BooleanField(default=True)),
                ("depended_upon", models.BooleanField(default=False)),
                ("status", models.BooleanField(default=True)),
                ("comment", models.TextField(blank=True, max_length=150, null=True)),
                ("create_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("modify_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "GWM_apk",
                "verbose_name_plural": "GWM_apks",
                "db_table": "gwm_apk",
                "unique_together": {("name",)},
            },
        ),
    ]
