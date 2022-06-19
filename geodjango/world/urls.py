from django.urls import path

from world.views import MarkersMapView
from world.views import show, mapview, edit, delete, create, add

app_name = "world"

urlpatterns = [
    path("map/<str:name>", MarkersMapView.as_view()),
    path("show/", show),
    path("", show),
    path("edit", edit),
    path("delete/<str:id>", delete),
    path("create", create),
    path("add/", add),


    # path("random/<str:name", mapview)
]
