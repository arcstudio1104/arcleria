from django.contrib import admin
from .models import Faq, Flatpage, BannerGallery, BannerHome

admin.site.site_header = 'arcleria 관리자'
admin.site.site_title = 'arcleria 관리자'


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['order', 'title', 'category']
    list_filter = ['category']


@admin.register(Flatpage)
class FlatpageAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(BannerHome)
class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = []
    list_display = ['id', 'image', 'image_m', 'redirect_url']
    list_filter = []
    fieldsets = [
        ('기본 데이터', {'fields': [
            'image', 'image_m', 'redirect_url',
        ]}),
    ]


@admin.register(BannerGallery)
class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = []
    list_display = ['id', 'image', 'image_m', 'name', 'place', 'exhibition', 'date', 'redirect_url']
    list_filter = []
    search_fields = ['name']
    fieldsets = [
        ('기본 데이터', {'fields': [
            'image', 'image_m', 'name', 'place', 'exhibition', 'date', 'redirect_url'
        ]}),
    ]