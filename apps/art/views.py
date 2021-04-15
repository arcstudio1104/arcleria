from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Picture, Exhibition, Gallery, Artist, Tag
from apps.blog.models import BannerGallery


def picture_list(request):
    picture = Picture.objects.all()
    paginator = Paginator(picture, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'picture/list.html', context)


def picture_detail(request, pk):
    picture = get_object_or_404(Picture, id=pk)
    picture_gallery = Picture.objects.exclude(Q(id=pk) | Q(is_sale=True) | Q(gallery__isnull=True)).filter(gallery=picture.gallery)
    picture_artist = Picture.objects.exclude(Q(id=pk) | Q(is_sale=True) | Q(artist__isnull=True)).filter(artist=picture.artist)
    picture_similar = Picture.objects.exclude(Q(id=pk) | Q(is_sale=True)).filter(kind=picture.kind).order_by('?')[0:20]
    context = {'object': picture, 'picture_gallery': picture_gallery, 'picture_artist': picture_artist, 'picture_similar': picture_similar}
    return render(request, 'picture/detail.html', context)


def exhibition_list(request):
    exhibition = Exhibition.objects.filter(is_end=False)
    exhibition_end = Exhibition.objects.filter(is_end=True)
    paginator = Paginator(exhibition, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'exhibition_end': exhibition_end}
    return render(request, 'exhibition/list.html', context)


def gallery_list(request):
    banner = BannerGallery.objects.all()
    gallery = Gallery.objects.all()
    paginator = Paginator(gallery, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'banner': banner}
    return render(request, 'gallery/list.html', context)


def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, id=pk)
    exhibition = Exhibition.objects.filter(is_end=False, gallery=gallery)
    exhibition_end = Exhibition.objects.filter(is_end=True, gallery=gallery)
    picture = Picture.objects.filter(gallery=gallery)
    context = {'object': gallery, 'exhibition': exhibition, 'exhibition_end': exhibition_end, 'picture': picture}
    return render(request, 'gallery/detail.html', context)


def artist_list(request):
    artist = Artist.objects.all()
    artist_popular = Artist.objects.filter(is_popular=True)
    paginator = Paginator(artist, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'artist_popular': artist_popular}
    return render(request, 'artist/list.html', context)


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    artist_tag = Tag.objects.filter(artist=artist)
    artist_picture = Picture.objects.filter(artist=artist)
    paginator = Paginator(artist_picture, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'object': artist, 'page_obj': page_obj, 'artist_tag': artist_tag}
    return render(request, 'artist/detail.html', context)




