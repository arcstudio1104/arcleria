from __future__ import unicode_literals
from django.conf import settings


CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER = getattr(settings, 'CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER', '+82')

CONTACT_VERIFICATION_SMS_TEXT = getattr(settings, 'CONTACT_VERIFICATION_SMS_TEXT', '{code}')

CONTACT_VERIFICATION_SENDER = getattr(settings, 'CONTACT_VERIFICATION_SENDER', '0000')

CONTACT_VERIFICATION_ALLOW_MULTIPLE_CONTACTS = getattr(settings, 'CONTACT_VERIFICATION_ALLOW_MULTIPLE_CONTACTS', False)

CONTACT_VERIFICATION_ALLOW_CONTACT_OVERRIDE = getattr(settings, 'CONTACT_VERIFICATION_ALLOW_CONTACT_OVERRIDE', False)

CONTACT_VERIFICATION_PROVIDER = getattr(settings, 'CONTACT_VERIFICATION_PROVIDER', 'coolsms')

CONTACT_VERIFICATION_COOLSMS_API_KEY = getattr(settings, 'CONTACT_VERIFICATION_COOLSMS_API_KEY', '')

CONTACT_VERIFICATION_COOLSMS_API_SECRET = getattr(settings, 'CONTACT_VERIFICATION_COOLSMS_API_SECRET', '')