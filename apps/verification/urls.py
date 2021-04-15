# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'pins', views.ContactVerificationViewSet)
router.register(r'contacts', views.ContactViewSet)
# router.register(r'countries', views.CountryViewSet, base_name='countries')  # base_name 더이상 사용 안함
router.register(r'countries', views.CountryViewSet, basename='countries')  # 최신버전 리눅스 2.9.7

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^countries/$', views.CountryList.as_view(), name="country-list"),
]
