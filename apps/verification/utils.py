from apps.verification.models import ContactVerification, Contact
from apps.verification.serializers import minify_phone_number
from apps.verification.settings import CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER, CONTACT_VERIFICATION_ALLOW_MULTIPLE_CONTACTS


def is_contact_valid(phone_number, code, country_number=None):
    if not country_number:
        country_number = CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER

    kwargs = {
        'country_number': country_number,
        'phone_number': minify_phone_number(phone_number),
        'code': code,
    }

    # return ContactVerification.objects.awaiting().filter(**kwargs).exists()
    return ContactVerification.objects.filter(**kwargs).exists()


def create_contact(user, phone_number, country_number=None):
    if not country_number:
        country_number = CONTACT_VERIFICATION_DEFAULT_COUNTRY_NUMBER

    phone_number = minify_phone_number(phone_number)

    if not CONTACT_VERIFICATION_ALLOW_MULTIPLE_CONTACTS:
        user.contacts.all().delete()

    return Contact.objects.get_or_create(user=user, phone_number=phone_number, country_number=country_number)