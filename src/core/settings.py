from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-reuy-jgd^ecq&-sv%@*j^p!l(een^w4d+9e@3_6#cny+-ml2hb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django_ckeditor_5',
    'modeltranslation',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'corsheaders',
    'whitenoise',

    'account',
    'cours',
    'utils',
    'news',
    'tesol',
    'django_filters',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # translate
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.default_language.CustomLocaleMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('uz', 'en', 'ru')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('uz', 'en', 'ru')

MODELTRANSLATION_TRANSLATION_FILES = (
    'cours.translation.translate',
    'utils.translation.translate',
    'news.translation.translate',
    'tesol.translation.translate',
)

LANGUAGE_CODE = 'en-us'

gettext = lambda s: s

LANGUAGES = (
    ('uz', gettext("O'zbek tili")),
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'

CKEDITOR_UPLOAD_PATH = "uploads/"
# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

HOST = 'https://4f8d-213-230-69-88.ngrok-free.app'

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = [HOST]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
}
AUTH_USER_MODEL = "account.User"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
}

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': ['heading', '|', 'bold', 'italic', 'link',
                      'bulletedList', 'numberedList', 'blockQuote', 'imageUpload'],
        }
    },
    'extends': {  # ❗ BU NOM AYNAN SHU BO'LISHI KERAK
        'toolbar': {
            'items': ['heading', '|', 'bold', 'italic', 'link',
                      'bulletedList', 'numberedList', 'blockQuote', 'imageUpload',
                      'fontColor', 'fontBackgroundColor', 'insertTable', 'undo', 'redo',
                      'mediaEmbed', 'horizontalLine', 'codeBlock', 'code', 'removeFormat'],
        },
        # qo‘shimcha sozlamalar
    }
}

# CK_EDITOR_5_UPLOAD_FILE_VIEW_NAME = "custom_upload_file"
CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"  # Possible values: "staff", "authenticated", "any"

JAZZMIN_SETTINGS = {
    "site_title": "Admin Panel",
    "site_header": "Tesol boshqaruvi",
    "site_brand": "Tesol",
    "login_logo": "images/logo.png",
    "site_icon": "images/favicon.ico",

    "welcome_sign": "Xush kelibsiz, foydalanuvchi!",

    "search_model": ["account.User"],

    "topmenu_links": [
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},
        # {"model": "account.User"},

    ],
    "usermenu_links": [
        {"name": "Tesol", "url": "https://tesol.international", "new_window": True},
        {"name": "Nr Hub", "url": "https://nrvisionhub.com/", "new_window": True},
    ],
    "custom_js": "admin/js/language_switcher.js",

    "show_sidebar": True,
    "navigation_expanded": True,

    "hide_apps": [],
    "hide_models": [],

    "order_with_respect_to": ["account", "app", "cours", "news", "tesol", "gallery"],

    "icons": {
        "account": "fas fa-users-cog",
        "account.User": "fas fa-user",
        "auth.group": "fas fa-users",
        "news.News": "fas fa-newspaper",
        "news.About": "far fas fa-info-circle",
        "tesol.About": "fas fa-info-circle",
        "tesol.Teachers": "fas fa-chalkboard-teacher",
        "tesol.Partners": "fas fa-handshake",
        "tesol.Courses": "fas fa-book-reader",
        "tesol.Services": "fas fa-concierge-bell",
        "tesol.Accreditation": "fas fa-certificate",
        "tesol.CourseType": "fas fa-tags",
        "tesol.Settings": "fas fa-cogs",
        "tesol.News": "fas fa-newspaper",
        "tesol.Gallery": "fas fa-images",
        "tesol.GalleryCategory": "fas fa-folder-open",
        "tesol.GalleryView": "fas fa-eye",
        "utils.About": "fas fa-info-circle",
        "utils.Settings": "fas fa-cogs",
        "cours.CourseType": "fas fa-tags",
        "cours.Courses": "fas fa-book-reader",
        # "cours.CoursesTeachers": "fas fa-chalkboard-teacher",

    },

    "default_icon_parents": "fas fa-folder-open",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": False,
    "custom_css": None,
    # "custom_js": None,

    "show_ui_builder": False,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    # "dark_mode_theme": "darkly",
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark bg-primary",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_flat_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_child_hide_on_collapse": True,
    "sidebar_nav_icon": "fas fa-circle",
    "actions_sticky_top": True,
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kamezukashidev@gmail.com'
EMAIL_HOST_PASSWORD = 'otcibxgrfbcyjwqu'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

FRONTEND_URL = 'https://b89f-213-230-69-88.ngrok-free.app'
