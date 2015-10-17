"""
WSGI config for Zastosowanie_informatyki_w_gospodarce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Zastosowanie_informatyki_w_gospodarce.settings")

application = get_wsgi_application()
