# ==================================================
# Django 設定
# ==================================================
import os

# プロジェクトディレクトリ設定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# セキュリティキー設定
SECRET_KEY = os.environ.get('SECRET_KEY')

# デバッグモード設定
DEBUG = int(os.environ.get('DEBUG', default=0))

# 許可するホストを記載
ALLOWED_HOSTS = ['web']

# --------------------------------------------------
# アプリケーション定義
# --------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# --------------------------------------------------
# データベース定義
# --------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DATABASE_DB', 'django_db'),
        'USER': os.environ.get('DATABASE_USER', 'django_db_user'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'django_db_pass'),
        'HOST': os.environ.get('DATABASE_HOST', 'db'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}


# --------------------------------------------------
# パスワード確認
# --------------------------------------------------
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


# --------------------------------------------------
# 国際化
# --------------------------------------------------
LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# --------------------------------------------------
# 静的ファイル（CSS, JavaScript, Images）
# --------------------------------------------------
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
