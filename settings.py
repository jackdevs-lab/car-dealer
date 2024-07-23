from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&3ima5uzm&-j&bv+u1eg_qz4u3$^sz8x7hlqc5di0yj^_r-4ax'
# with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
#     SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
# Deploying on render cloud host
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    # 'django_crontab', #for scheduled job specially for backup database
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'car.apps.CarConfig',
    'django.contrib.humanize', # used in templates, html files-> adds coma to numbers
    # 'import_export', # import export csv file button in django admin section
    # 'dbbackup',  # django-dbbackup
]

# django-dbbackup
# https://django-dbbackup.readthedocs.io/en/master/installation.html
# DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
# DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR/'backup'}

# django crontab job scheduling
# does NOT work on windows
# CRONJOBS = [
#     ('*/1 * * * *', 'cardealer.cron.my_scheduled_job')
# ]   # some crontab terminal commands 
# https://pypi.org/project/django-crontab/
# python manage.py crontab add
# python manage.py crontab show
# python manage.py crontab remove


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cardealer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # added templates path
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'car.context_processors.ad_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'cardealer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# database for cloud deployment
# DATABASES = {
#     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
# } #Now set this DATABASE_URL variable on cloud service


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")  #Not used on localhost
# addr for static files of templates


#This should be not used on AWS
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# add media files so that car pictures can be seen by url.

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


#temp
# RuntimeError at /submit_number/3
# You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SLASH set. 
# Django can't redirect to the slash URL while maintaining POST data. 
# Change your form to point to 127.0.0.1:8000/submit_number/3/ (note the trailing slash),
#  or set APPEND_SLASH=False in your Django settings.    
APPEND_SLASH=False



# HTTPS settings for production
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE: ensures a secure session cookie is used
# CSRF_COOKIE_SECURE: ensures a secure CSRF cookie is used
# SECURE_SSL_REDIRECT: all non-HTTP requests are redirect to HTTPS


# HSTS settings
# SECURE_HSTS_SECONDS = 31536000 # 1 year
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# SECURE_HSTS_SECONDS: prevents browsers from connecting to your website with an insecure connection for the specified duration in seconds
# SECURE_HSTS_PRELOAD: the preload directive is added to the HSTS header
# SECURE_HSTS_INCLUDE_SUBDOMAINS: the includeSubDomains directive is added to the HSTS header
