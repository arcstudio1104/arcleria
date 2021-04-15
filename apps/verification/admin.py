from django.contrib import admin
from .models import ContactVerification, Contact


@admin.register(ContactVerification)
class ContactVerificationAdmin(admin.ModelAdmin):
    list_display = ['country_number', 'phone_number', 'code', 'created']
    search_fields = ['phone_number']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'country_number', 'phone_number']
    search_fields = ['phone_number']