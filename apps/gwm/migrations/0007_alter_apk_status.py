# Generated by Django 4.2.16 on 2024-12-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gwm", "0006_remove_apk_file_sha256_apk_file_md5"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apk",
            name="status",
            field=models.CharField(
                choices=[("public", "Public"), ("draft", "Draft")],
                default="public",
                max_length=10,
            ),
        ),
    ]