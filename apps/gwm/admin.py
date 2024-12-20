from django.contrib import admin
from .models import *


@admin.register(Apk)
class ApkAdmin(admin.ModelAdmin):
    search_fields = ("name", "version", "file_md5", "comment")
    list_display = [
        "name",
        "version",
        "is_update",
        "force_update",
        "locked",
        "status",
        "file_md5",
        "file_size",
        "comment",
        "create_at",
        "modify_at"
    ]
