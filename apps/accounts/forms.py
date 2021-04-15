from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm as BaseSetPasswordForm, PasswordChangeForm as BasePasswordChangeForm
from django.utils.safestring import mark_safe

from apps.verification.utils import create_contact, is_contact_valid

User = get_user_model()


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label="비밀번호 *", widget=forms.PasswordInput(attrs={'placeholder': "8~32자리의 영문, 숫자 혼합"}))
    password2 = forms.CharField(label="비밀번호 확인 *", widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 한 번 더 입력해주세요.'}))
    email = forms.EmailField(label="아이디 (이메일) *", widget=forms.EmailInput(attrs={'placeholder': 'arcleria@gmail.com'}), help_text="반드시 실제로 사용하시는 이메일을 입력해주세요!")
    username = forms.CharField(label="이름 *", widget=forms.TextInput(attrs={'placeholder': "홍길동", 'maxlength': 10}), help_text="고객님의 성함을 입력해주세요.")
    phone_number = forms.CharField(label="휴대폰 *", widget=forms.TextInput(attrs={'placeholder': "휴대폰 번호 \'-\' 없이 입력"}))
    code = forms.CharField(label="인증번호")

    is_agreed_1 = forms.BooleanField(label=mark_safe("<div style='position:relative; top:-1px; left:5px'>[필수] <a href='/blog/terms' class='text-primary'>이용약관</a> 및 <a href='/blog/privacy' class='text-primary'>개인정보처리방침</a>에 동의</div>"))
    marketing = forms.BooleanField(label=mark_safe("<div style='position:relative; top:-1px; left:5px'>[선택] <a href='/blog/privacy' class='text-primary'>광고성 정보 수신</a> 동의</div>"), required=False)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2',
            'phone_number',
            'code',
            'is_agreed_1',
            'marketing',
        ]
        help_texts = {


        }
        widgets = {

        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password2

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("phone_number")
        code = cleaned_data.get("code")
        if phone_number and code and not is_contact_valid(phone_number, code):
            self.add_error('code', _("인증번호 또는 전화번호가 올바르지 않습니다."))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            create_contact(user, self.cleaned_data['phone_number'])
        return user


class SetPasswordForm(BaseSetPasswordForm):
    new_password1 = forms.CharField(
        label="새 비밀번호",
        widget=forms.PasswordInput(attrs={'placeholder': "8~32자리의 영문, 숫자를 혼합하여 사용하세요."}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="새 비밀번호 확인",
        strip=False,
        widget=forms.PasswordInput,
    )


class PasswordChangeForm(BasePasswordChangeForm):
    old_password = forms.CharField(
        label='기존 비밀번호',
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.PasswordInput(attrs={'placeholder': '8~32자리의 영문, 숫자를 혼합하여 사용하세요.'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label='새 비밀번호 확인',
        strip=False,
        widget=forms.PasswordInput,
    )