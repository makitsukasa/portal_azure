"""
WSGI config for quickstartproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from wsgi_basic_auth import BasicAuth

settings_module = 'quickstartproject.production' if 'WEBSITE_HOSTNAME' in os.environ else 'quickstartproject.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = BasicAuth(get_wsgi_application())
