from django.urls import reverse_lazy
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import PasswordResetConfirmView as BasePasswordResetConfirmView, PasswordChangeView as BasePasswordChangeView
from django.views.generic import CreateView

from .forms import UserCreateForm, SetPasswordForm, PasswordChangeForm


User = get_user_model()


class UserCreate(CreateView):
    template_name = 'registration/user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class PasswordResetConfirmView(BasePasswordResetConfirmView):
    form_class = SetPasswordForm


class PasswordChangeView(BasePasswordChangeView):
    form_class = PasswordChangeForm
