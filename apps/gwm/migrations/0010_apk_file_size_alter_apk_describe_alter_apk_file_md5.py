# Generated by Django 4.2.16 on 2024-12-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gwm", "0009_remove_apk_depended_upon"),
    ]

    operations = [
        migrations.AddField(
            model_name="apk",
            name="file_size",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name="apk",
            name="describe",
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name="apk",
            name="file_md5",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]