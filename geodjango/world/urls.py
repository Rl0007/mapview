from django.urls import path

from world.views import MarkersMapView
from world.views import show, mapview

app_name = "world"

urlpatterns = [
    path("map/<str:name>", MarkersMapView.as_view()),
    path("show/", show),
    path("", show),
    # path("random/<str:name", mapview)
]
