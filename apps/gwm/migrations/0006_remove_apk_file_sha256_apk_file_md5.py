# Generated by Django 4.2.16 on 2024-12-18 01:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("gwm", "0005_remove_apk_file_md5_alter_apk_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="apk",
            name="file_sha256",
        ),
        migrations.AddField(
            model_name="apk",
            name="file_md5",
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]
