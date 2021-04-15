import os
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ka7n=+j)a=(hgmcu7+#b@6^81f6#qa-40xgl-11gh@6o!f=0)#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'bootstrap4',
    'ckeditor',
    'ckeditor_uploader',

    # Social login
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

    'apps.accounts',
    'apps.blog',
    'apps.art',
    'apps.verification',
    'apps.transaction',
]

# allauth 더하기
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1
LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = reverse_lazy('home')

# 구글 로그인 이메일 수집
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'arcleria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'arcleria.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
AUTH_USER_MODEL = 'accounts.User'


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# Media URL
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# django ckeditor
# https://github.com/django-ckeditor/django-ckeditor
CKEDITOR_UPLOAD_PATH = 'media/'


# Email
# 계정 보안 수준 - 낮음 / IMAP 사용 설정 필수
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'arcleria.bot@gmail.com'
EMAIL_HOST_PASSWORD = 'dkzmtmxbeldh13!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# CoolSMS 가입 인증
CONTACT_VERIFICATION_SMS_TEXT = '[아클레리아] 인증번호는 [{code}]입니다.'
CONTACT_VERIFICATION_PROVIDER = 'coolsms'
CONTACT_VERIFICATION_SENDER = '01084647744'
CONTACT_VERIFICATION_COOLSMS_API_KEY = 'NCSFJOJLFMVZHXHS'
CONTACT_VERIFICATION_COOLSMS_API_SECRET = 'XV5NEWVFIKAAUPBVAYIKQ8SYLLYDOCMV'


# 아임포트
IAMPORT_MID = 'imp56239470'
IAMPORT_API_KEY = '5107141407270250'
IAMPORT_API_SECRET = 'q6o5pS1022NetVIwEWjG9RHIxX4toNtPTSUjLWjOY72r2KYHGinPa4yH2DbqqFfjy9Dk6W844aw7VvOB'