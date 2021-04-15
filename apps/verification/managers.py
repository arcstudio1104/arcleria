from django.db import models
from django.utils import timezone


class ContactVerificationQuerySet(models.QuerySet):
    def awaiting(self):
        expiry_datetime = timezone.now()-timezone.timedelta(minutes=3)
        return self.filter(created__gte=expiry_datetime)

    def inactive(self):
        expiry_datetime = timezone.now()-timezone.timedelta(minutes=3)
        return self.filter(created__lt=expiry_datetime)
