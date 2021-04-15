# coding=utf-8
from __future__ import unicode_literals
from random import randint

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.verification.data import COUNTRY_PHONES
from apps.verification.settings import CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER
from apps.verification.validators import PhoneNumberValidator
from .managers import ContactVerificationQuerySet


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="contacts", on_delete=models.CASCADE)
    country_number = models.CharField(max_length=10, choices=COUNTRY_PHONES, blank=True)
    phone_number = models.CharField(max_length=100, validators=[PhoneNumberValidator()])

    class Meta:
        verbose_name = _("연락처")
        verbose_name_plural = _("연락처")

    def __unicode__(self):
        return "{}-{}".format(self.country_number, self.phone_number)

    def get_full_number(self, exclude_country=False):
        if exclude_country:
            return "0"+self.phone_number
        elif self.country_number == "+82":
            return "0"+self.phone_number
        else:
            return self.country_number + "-" + self.phone_number

    def get_country_number(self):
        return self.country_number

    def get_phone_number(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        if not self.country_number:
            self.country_number = CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER
        if self.phone_number and self.phone_number[0] == '0':
            self.phone_number = self.phone_number[1:]

        super(Contact, self).save(*args, **kwargs)


class ContactVerification(models.Model):
    country_number = models.CharField(max_length=10, choices=COUNTRY_PHONES, blank=True)
    phone_number = models.CharField(max_length=100, validators=[PhoneNumberValidator()])
    code = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    objects = ContactVerificationQuerySet.as_manager()

    class Meta:
        verbose_name = _("연락처 인증")
        verbose_name_plural = _("연락처 인증")

    def __unicode__(self):
        return "{}{}".format(self.country_number, self.phone_number)

    @staticmethod
    def generate_code():
        return str(randint(10000, 99999))

    def is_awaiting(self):
        return ContactVerification.objects.awaiting().filter(id=self.id).exists()

    def get_full_number(self, exclude_country=False):
        if exclude_country:
            return "0" + self.phone_number
        elif self.country_number == "+82":
            return "0" + self.phone_number
        else:
            return self.country_number + "-" + self.phone_number

    def get_country_number(self):
        return self.country_number

    def get_phone_number(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        if not self.country_number:
            self.country_number = CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER
        if self.phone_number and self.phone_number[0] == '0':
            self.phone_number = self.phone_number[1:]

        pin_exists = ContactVerification.objects.awaiting().filter(
            country_number=self.country_number, phone_number=self.phone_number
        ).exists()

        if not pin_exists:
            if not self.code:
                self.code = ContactVerification.generate_code()

            super(ContactVerification, self).save(*args, **kwargs)
