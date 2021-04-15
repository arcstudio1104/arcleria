from django.urls import path

from . import views

urlpatterns = [
    path('picture/list', views.picture_list, name='picture_list'),
    path('picture/<int:pk>', views.picture_detail, name='picture_detail'),
    path('exhibition', views.exhibition_list, name='exhibition_list'),
    path('gallery', views.gallery_list, name='gallery_list'),
    path('gallery/<int:pk>', views.gallery_detail, name='gallery_detail'),
    path('artist', views.artist_list, name='artist_list'),
    path('artist/<int:pk>', views.artist_detail, name='artist_detail'),
]

