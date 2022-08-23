# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a07=uubowmpe3op(az#%rzzhr+5!@lx31q7l#t$$cn#-amt)m4'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}