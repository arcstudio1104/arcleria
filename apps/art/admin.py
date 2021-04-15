from django.contrib import admin

from .models import Artist, Gallery, Picture, Exhibition, Tag


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = []
    list_display = ['name', 'native', 'birth_year', 'like', 'is_popular']
    list_filter = []
    search_fields = ['name']
    fieldsets = [
        ('기본 데이터', {'fields': [
            'name', 'introduce', 'image', 'is_popular',
        ]}),
        ('추가 데이터', {'fields': [
            'native', 'birth_year', 'belong', 'award', 'collection', 'exhibition_history', 'like'
        ]}),
    ]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = []
    list_display = ['name', 'place', 'like']
    list_filter = []
    search_fields = ['name']
    fieldsets = [
        ('기본 데이터', {'fields': [
            'name', 'place', 'introduce', 'image_1',
        ]}),
        ('추가 데이터', {'fields': [
            'like', 'image_2', 'image_3',
        ]}),
    ]


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    readonly_fields = []
    list_display = ['name', 'artist', 'gallery', 'price', 'shipping_fee', 'size_horizontal', 'size_vertical', 'like', 'is_sale', 'buy_process']
    list_filter = ['artist', 'gallery']
    search_fields = ['name', 'artist', 'gallery']
    fieldsets = [
        ('기본 데이터', {'fields': [
            'name', 'artist', 'gallery', 'make_year', 'size_horizontal', 'size_vertical', 'kind', 'material', 'introduce', 'image_1',
        ]}),
        ('추가 데이터', {'fields': [
            'like', 'recommend_reason', 'image_2', 'image_3', 'image_4', 'image_5',
        ]}),
        ('판매 데이터', {'fields': [
             'price', 'shipping_fee', 'is_sale', 'buy_process'
        ]}),
    ]


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    readonly_fields = []
    list_display = ['name', 'gallery', 'place', 'date_start', 'date_end', 'is_end']
    list_filter = ['gallery']
    search_fields = ['name', 'gallery']
    fieldsets = [
        ('기본 데이터', {'fields': [
            'is_end', 'name', 'place', 'date_start', 'date_end', 'image_1', 'redirect_url'
        ]}),
        ('추가 데이터', {'fields': [
            'gallery',
        ]}),
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = []
    list_display = ['id', 'artist', 'tag']
    list_filter = []
    fieldsets = [
        ('기본 데이터', {'fields': [
            'artist', 'tag'
        ]}),
    ]