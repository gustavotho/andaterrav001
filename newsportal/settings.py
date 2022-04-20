import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#verifica se a aplicação está rodando na maquina local ou em produção
if str(BASE_DIR)[:24] == '/home/gustavo/workspace/':
    local = True
else:
    local = False


SECRET_KEY = '08nva+ja-kswomarqd*i5bcx+@e&)$uo6nsxmmfarukp04^k_ackz&0r*8('

# SECURITY WARNING: don't run with debug turned on in production!

if local:
    DEBUG = True
else:
    DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'news',
    'cat',
    'subcat',
    'contactform',
    'trending',
    'manager',
    'newsletter',
    'django.contrib.humanize',
    'comment',
    'blacklist',
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

ROOT_URLCONF = 'newsportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'main/templates/front'),
            os.path.join(BASE_DIR, 'main/templates/front/base'),
        ],
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

WSGI_APPLICATION = 'newsportal.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS' : {
            'options': '-c search_path=public'
        },
        'NAME': 'andaterra_news',
        'USER': 'andaterra_news_user',
        'PASSWORD': 'zicaK7cu',
        'HOST': '142.4.219.195',
        'PORT': '5432',
    },
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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Bahia'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = ['%d/%m/%Y','%d-%m-%Y']

DATE_FORMAT = '%d/%m/%Y'



#RESOLVENDO O PROBLEMA DA INCONSISTENCIA DA PASTA STATIC
if local:
    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    ]

    # Media Files
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

else:
    STATIC_URL = '/static'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')   # address of the folder


    # Media Files
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


## Do it later - Not done yet
# Cron Tab
# CRONJOBS = [  # for 5 minutes
#     ('*/5 * * * *' , 'main.cron.my_job') # here main is an app where i created cron.py file
# ]
