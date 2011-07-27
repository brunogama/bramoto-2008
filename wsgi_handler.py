#!/usr/bin/python

import sys
import os

altpath = sys.path
sys.path = ['/Users/bruno/dev/lib/python/extras']
sys.path += ['/Users/bruno/dev/lib/python/extras']
sys.path += ['/Users/bruno/dev/lib/python/django_src']
sys.path += ['/Users/bruno/dev/www/python/django']
sys.path += altpath 


os.environ['DJANGO_SETTINGS_MODULE'] = 'bramoto.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()