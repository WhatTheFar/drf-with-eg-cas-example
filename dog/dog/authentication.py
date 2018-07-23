from django.contrib.auth.middleware import RemoteUserMiddleware
from rest_framework.authentication import RemoteUserAuthentication


class CustomHeaderMiddleware(RemoteUserMiddleware):
    header = 'HTTP_AUTH_USER'


class CustomHeaderAuthentication(RemoteUserAuthentication):
    header = 'HTTP_AUTH_USER'
