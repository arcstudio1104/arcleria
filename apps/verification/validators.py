# coding=utf-8
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class PhoneNumberValidator(RegexValidator):
    regex = r'^[0-9]*$'
    message = _('숫자만 입력해주세요.')
