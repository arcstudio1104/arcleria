from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm

from apps.verification.models import Contact


User = get_user_model()


class UserCreateAdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0
    min_num = 1
    max_num = 1
    readonly_fields = ['country_number', 'phone_number']


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # 배포전 관리자 변경 불가필드 반드시 지정
    # readonly_fields = ['email', 'username', 'phone_number', 'marketing', 'is_staff', 'is_superuser', 'groups']
    list_display = ['id', 'email', 'username', 'phone_number', 'marketing', 'is_staff', 'created']
    list_filter = ['is_active']
    search_fields = ['username', 'email']
    ordering = ['id']
    inlines = [ContactInline]

    add_form = UserCreateAdminForm
    add_form_template = 'admin/change_form.html'
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    fieldsets = [
        ('기본정보', {'fields': [
            'email',
            'username',
            'password',
        ]}),
        ('개인정보', {'fields': [
            'phone_number',
            'marketing',
        ]}),
        ('권한', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
        )})
    ]
