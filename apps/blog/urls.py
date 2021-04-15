from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about_us_view, name='about_us'),
    path('faq/<slug:category>', views.faq_search, name='search_faq'),
    path('terms', views.Terms.as_view(), name='terms'),
    path('privacy', views.Privacy.as_view(), name='privacy'),
]
