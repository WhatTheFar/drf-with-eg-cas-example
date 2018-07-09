from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from hello import viewsets

router = DefaultRouter()
router.register(r'dog', viewsets.DogViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
