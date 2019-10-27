"""
WSGI config for Report project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from os.path import join,dirname,abspath
from django.core.wsgi import get_wsgi_application

PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys # 4
sys.path.insert(0,PROJECT_DIR) # 5
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Report.settings')

application = get_wsgi_application()
