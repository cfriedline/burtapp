# BURTapp

This is the code to build out the site, BURTapp (Barking Up the Right Trees) for the [NSF project #1306622](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1306622).

##Architecture

`client <--> nginx <--> uWSGI <--> Django <--> PostgresSQL`

##Setup

1. Create a new conda environment for the project: `conda env create --file environment.yml`
2. Adjust the paths, etc in the django.nginx file and copy to your sites-enabled
3. Adjust the paths in uwsgi.ini.  I'm running it in emporer mode from `rc.local` as `uwsgi --emperor /etc/uwsgi/vassals > /dev/null 2>&1 &`.  The ini file is symlinked in `vassals`
4. You'll need a settings.py file in `./burt`.  See below   
5. Run the dev server: `make runserver`
6. If all is well, collect static files: `make static`

##Example settings.py
<pre>
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = (
    'bootstrap3',
    'django_extensions',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'envdata'
    )

MIDDLEWARE_CLASSES = (
    'sslifyadmin.middleware.SSLifyAdminMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'burt.urls'
WSGI_APPLICATION = 'burt.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '[db]',
        'USER': '[user]',
        'PASSWORD': '[user]',
        'HOST':'localhost',
        'PORT':'5432'
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
GRAPPELLI_ADMIN_TITLE = 'BURTApp Admin'
SSLIFY_ADMIN_DISABLE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
</pre>
