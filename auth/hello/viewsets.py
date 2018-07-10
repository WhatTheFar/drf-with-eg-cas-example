from rest_framework import permissions
from rest_framework import viewsets

from hello.models import Auth
from hello.serializers import AuthSerializer


class AuthViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AuthSerializer
    queryset = Auth.objects.all()
