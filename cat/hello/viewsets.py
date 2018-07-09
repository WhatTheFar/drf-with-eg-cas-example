from rest_framework import viewsets
from rest_framework import permissions

from hello.models import Cat
from hello.serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CatSerializer
    queryset = Cat.objects.all()
