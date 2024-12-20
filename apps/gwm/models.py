from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from django.db.models import F
import uuid
import logging

logger = logging.getLogger(__name__)

"""
Haval H6/Dagou / Tank300:
endpoint: /apiv2/car_apk_update

"""

class Apk(models.Model):
    STATUS_CHOICES = (
        ('public', 'Public'),
        ('draft', 'Draft'),
    )
    id = models.CharField(max_length=90, default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    version = models.CharField(max_length=20, null=False, blank=False)
    describe = models.CharField(max_length=60, null=True, blank=True)
    file_url = models.TextField(max_length=300, blank=False, null=False)
    file_md5 = models.CharField(max_length=120, null=True, blank=True)
    file_size = models.CharField(max_length=90, null=True, blank=True)
    is_update = models.BooleanField(default=True)
    force_update = models.BooleanField(default=True)
    locked = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='public')
    comment = models.TextField(max_length=150, blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now)
    modify_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("gwm_apk")
        verbose_name_plural = _("gwm_apks")
        unique_together = [("name", )]
        db_table = "gwm_apk"

    def save(self, *args, **kwargs):
        if self.locked:
            with transaction.atomic():
                updated_count = Apk.objects.filter(locked=True).exclude(pk=self.pk).update(locked=False)
                if updated_count > 0:
                    logger.warning(f"Updated {updated_count} records to set locked as False")
        super(Apk, self).save(*args, **kwargs)

    def __str__(self):
        return "{}/{} - update:{}".format(self.name, self.version, self.is_update)
