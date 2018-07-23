from rest_framework import permissions
from rest_framework import viewsets

from hello.models import Dog
from hello.serializers import DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
