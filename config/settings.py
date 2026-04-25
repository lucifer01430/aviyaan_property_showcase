from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-change-this-later'
DEBUG = True
ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.core',
    'apps.showcase',
    'apps.dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'apps.core.context_processors.site_settings',
        ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = []


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "Aviyaan Admin",
    "site_header": "Aviyaan",
    "site_brand": "Aviyaan",
    "site_logo": None,
    "login_logo": None,
    "site_icon": None,
    "login_logo_dark": None,
    "user_avatar": None,
    "site_logo_classes": "img-circle",    
    "welcome_sign": "Welcome to Aviyaan Showcase Admin",
    "copyright": "Aviyaan Showcase",
    "search_model": ["showcase.Segment","core.SiteSetting"],


    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["showcase", "core", "auth"],

    "icons": {
        "auth": "fas fa-user-shield",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",

        "core": "fas fa-sliders-h",
        "core.sitesetting": "fas fa-cog",

        "showcase": "fas fa-images",
        "showcase.segment": "fas fa-th-large",
        "showcase.segmentmedia": "fas fa-photo-video",
    },

    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "related_modal_active": True,
    "custom_css": "css/jazzmin_custom.css",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,

    "brand_colour": "navbar-dark",
    "accent": "accent-warning",

    "navbar": "navbar-white navbar-light",
    "no_navbar_border": True,
    "navbar_fixed": True,

    "layout_boxed": False,
    "footer_fixed": False,

    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,

    "theme": "flatly",
    "dark_mode_theme": None,

    "button_classes": {
        "primary": "btn btn-warning",
        "secondary": "btn btn-outline-secondary",
        "info": "btn btn-outline-info",
        "warning": "btn btn-warning",
        "danger": "btn btn-danger",
        "success": "btn btn-success"
    }
}