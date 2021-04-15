# coding=utf-8
from __future__ import unicode_literals
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apps.verification import settings
from apps.verification.models import ContactVerification, Contact
from apps.verification.settings import CONTACT_VERIFICATION_PROVIDER


def minify_phone_number(phone_number):
    if phone_number.isdigit() and len(phone_number) > 0 and phone_number[0] == '0':
        phone_number = phone_number[1:]
    return phone_number


def send_sms(body, body_en, pin, from_):
    provider = CONTACT_VERIFICATION_PROVIDER
    if provider == 'coolsms':
        try:
            api_key = settings.CONTACT_VERIFICATION_COOLSMS_API_KEY
            api_secret = settings.CONTACT_VERIFICATION_COOLSMS_API_SECRET
            client = Message(api_key, api_secret)

            country = pin.get_country_number()  # +82, +1 국가번호 리턴
            country_code = country.replace("+", "")  # + 제거

            if country_code == '82':
                to = pin.get_full_number(exclude_country=True)  # True is 한국 전용, 01045845505 형식으로 리턴
                kwargs = {'type': 'sms', 'to': to, 'from': from_, 'text': body}
                response = client.send(kwargs)
                return "error_list" not in response
            else:
                to = pin.get_phone_number()  # 1045845505 형식으로 리턴
                kwargs = {'type': 'sms', 'to': to, 'from': from_, 'text': body_en, 'country': country_code}
                response = client.send(kwargs)
                return "error_list" not in response

        except CoolsmsException as e:
            return False
    else:
        return False


class ContactVerificationSerializer(serializers.ModelSerializer):
    message = None

    class Meta:
        model = ContactVerification
        fields = ['country_number', 'phone_number']
        extra_kwargs = {
            'phone_number': {
                'error_messages': {'blank': _("전화번호를 입력하세요.")}
            }
        }

    def validate_phone_number(self, value):
        return minify_phone_number(value)

    def validate(self, attrs):
        ContactVerification.objects.inactive().delete()

        try:
            pin = ContactVerification.objects.get(**attrs)
        except ContactVerification.DoesNotExist:
            pin = None

        if pin and pin.is_awaiting():
            seconds = (timezone.timedelta(minutes=3)-(timezone.now() - pin.created)).seconds
            raise serializers.ValidationError(_("인증번호가 이미 전송되었습니다. %(seconds)s초 후에 재발송 가능합니다.") % {'seconds': seconds})

        if not settings.CONTACT_VERIFICATION_ALLOW_CONTACT_OVERRIDE:
            if Contact.objects.filter(**attrs).exists():
                raise serializers.ValidationError(_("이미 인증된 번호입니다."))

        return attrs

    def create(self, validated_data):
        instance = super(ContactVerificationSerializer, self).create(validated_data)

        message = settings.CONTACT_VERIFICATION_SMS_TEXT.format(code=instance.code)
        message_en = settings.CONTACT_VERIFICATION_SMS_TEXT_EN.format(code=instance.code)
        is_success = send_sms(message, message_en, instance, str(settings.CONTACT_VERIFICATION_SENDER))

        self.message = _("인증번호를 전송하였습니다.")
        """
        if is_success:
            self.message = _("인증번호를 전송하였습니다.")
        else:
            instance.delete()  # 현재 여기 문제 있음
            raise serializers.ValidationError({'message': _("인증번호 전송을 실패하였습니다.")})
        """
        return instance

    def to_representation(self, instance):
        ret = super(ContactVerificationSerializer, self).to_representation(instance)
        if self.message:
            ret['message'] = self.message
        return ret


class ContactSerializer(serializers.ModelSerializer):
    code = serializers.CharField(write_only=True, error_messages={'blank': _("인증번호를 입력하세요.")})

    class Meta:
        model = Contact
        fields = ['country_number', 'phone_number', 'code']
        extra_kwargs = {
            'phone_number': {
                'error_messages': {'blank': _("전화번호를 입력하세요.")}
            }
        }

    def validate_phone_number(self, value):
        return minify_phone_number(value)

    def validate(self, attrs):
        if not ContactVerification.objects.awaiting().filter(**attrs).exists():
            raise serializers.ValidationError(_("인증번호 또는 전화번호가 올바르지 않습니다."))
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        ContactVerification.objects.awaiting().filter(**validated_data).delete()

        if not settings.CONTACT_VERIFICATION_ALLOW_MULTIPLE_CONTACTS:
            user.contacts.all().delete()

        if settings.CONTACT_VERIFICATION_ALLOW_CONTACT_OVERRIDE:
            Contact.objects.filter(
                country_number=validated_data['country_number'],
                phone_number=validated_data['phone_number']
            ).delete()

        validated_data['user'] = user
        validated_data.pop('code', None)
        return super(ContactSerializer, self).create(validated_data)


class CountrySerializer(serializers.Serializer):
    number = serializers.CharField()
    name = serializers.CharField()
