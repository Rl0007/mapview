"""Markers API URL Configuration."""

from posixpath import basename
from rest_framework import routers
from django.urls import path

from world.viewset import WorldViewSet

router = routers.DefaultRouter()
# router.register("<int:name>", WorldViewSet)
router.register("Utah", WorldViewSet, basename='base')
urlpatterns = [
    path('world/<str:stname>',
         WorldViewSet.as_view({'get': 'list'})),
]
# router.register(
#     r'(?P<name>\d+)/world',
#     WorldViewSet
# )

urlpatterns += router.urls
