from .base import *  # NOQA
import sys
import logging.config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATES[0]["OPTIONS"].update({"debug": True})

# Turn off debug while imported by Celery with a workaround
# See http://stackoverflow.com/a/4806384

# Less strict password authentication and validation
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = []

#hosts
ALLOWED_HOSTS = ['*']

# Additional middleware introduced by debug toolbar


# Show emails to console in DEBUG mode
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Show thumbnail generation errors
THUMBNAIL_DEBUG = True

# Allow internal IPs for debugging
INTERNAL_IPS = ["127.0.0.1", "0.0.0.1"]

# Log everything to the logs directory at the top


# Reset logging
# (see http://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger/)

