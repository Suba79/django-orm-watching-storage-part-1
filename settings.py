from dotenv import load_dotenv
import os 


load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = ('SECRET_KEY', 'django-insecure-fallback-key-for-development')

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True