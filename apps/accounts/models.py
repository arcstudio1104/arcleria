from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    created = models.DateTimeField(verbose_name="가입일", auto_now_add=True)
    email = models.EmailField(verbose_name="이메일", unique=True)
    username = models.CharField(verbose_name="이름", max_length=10, blank=True)
    marketing = models.BooleanField(verbose_name="마케팅수신동의", default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = '회원'
        verbose_name_plural = '회원'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def phone_number(self):
        contact = self.contacts.first()
        return contact.get_full_number(exclude_country=False) if contact else None
    phone_number.fget.short_description = "휴대폰"

    @property
    def country_number(self):
        contact = self.contacts.first()
        return contact.get_country_number()