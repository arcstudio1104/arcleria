# coding=utf-8
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext as _

from .data import COUNTRY_PHONES
from .settings import CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER
from .validators import PhoneNumberValidator
from .models import ContactVerification, Contact


class ContactVerificationFormMixin(object):
    country_number = forms.ChoiceField(label='국가번호', choices=COUNTRY_PHONES, required=False)
    phone_number = forms.CharField(label='연락처', validators=[PhoneNumberValidator()])
    code = forms.CharField(label='인증번호')

    contacts = None

    class Media:
        js = ('/static/verification/verification.js',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        if user:
            self.contacts = user.contacts.all()
        super(ContactVerificationFormMixin, self).__init__(self, *args, **kwargs)

    def save(self, commit=True):
        instance = super(ContactVerificationFormMixin, self).save(commit)

        kwargs = {
            'user': instance,
            'country_number': self.cleaned_data.get('country_number', CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER),
            'phone_number': self.cleaned_data['phone_number']
        }

        Contact.objects.create(**kwargs)
        return instance

    def clean(self):
        cleaned_data = super(ContactVerificationFormMixin, self).clean()

        kwargs = {
            'country_number': cleaned_data.get('country_number', CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER),
            'phone_number': cleaned_data['phone_number'],
            'code': cleaned_data['code'],
        }

        # hook for extra contact verification validation
        self.clean_contact_verification(**kwargs)

        if not ContactVerification.objects.awaiting().filter(**kwargs).exists():
            self.add_error('code', _("인증번호 또는 전화번호가 올바르지 않습니다."))

    def clean_contact_verification(self, country_number, phone_number, code):
        pass
