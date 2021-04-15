from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator

from apps.art.models import Picture, Artist, Gallery, Exhibition
from apps.blog.models import Faq, Flatpage, BannerHome


def home_view(request):
    picture = Picture.objects.all()[0:12]
    artist = Artist.objects.all()[0:12]
    exhibition = Exhibition.objects.filter(is_end=False)[0:12]
    banner = BannerHome.objects.all()
    context = {'picture': picture, 'artist': artist, 'exhibition': exhibition, 'banner': banner}
    return render(request, 'home.html', context)


def about_us_view(request):
    return render(request, 'doc/about_us.html')


def faq_search(request, category):
    if category == 'all':
        faq = Faq.objects.all().order_by('order')
    else:
        faq = Faq.objects.filter(category=category).order_by('order')
    paginator = Paginator(faq, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'category': category}
    return render(request, 'blog/faq.html', context)


class Terms(ListView):
    template_name = 'doc/terms.html'
    queryset = Flatpage.objects.all()


class Privacy(ListView):
    template_name = 'doc/privacy.html'
    queryset = Flatpage.objects.all()