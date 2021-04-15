from django.urls import path
from . import views

urlpatterns = [
    path('ing/<int:pk>', views.cash_payment, name='cash_payment'),
]
