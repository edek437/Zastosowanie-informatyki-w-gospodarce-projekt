"""
WSGI config for Zastosowanie_medycyny_w_gospodarce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Zastosowanie_informatyki_w_gospodarce.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
