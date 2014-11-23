from .common import *

DEBUG = True
TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "../../db.sqlite3"),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = "/static/"

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "../templates"),
)

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = []
