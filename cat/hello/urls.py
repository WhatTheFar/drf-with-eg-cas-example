from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from hello import viewsets

router = DefaultRouter()
router.register(r'cat', viewsets.CatViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
