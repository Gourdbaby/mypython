"""
WSGI config for mypython project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mypython.settings")

application = get_wsgi_application()


# python服务器网关接口文件。相当于 python应用与web服务之间的接口
