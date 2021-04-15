from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.UserCreate.as_view(), name='user_create'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_change', views.PasswordChangeView.as_view(), name='password_change'),
]

