"""Markers API views."""
# from requests import request
# from requests import request
from rest_framework import viewsets
from rest_framework_gis import filters

from world.models import Admin1Us
from world.serializer import worldserializer


class WorldViewSet(viewsets.ModelViewSet):
    """Marker view set."""
    def para(request):
        print(request.GET('stname'))
    # para(request)

    def get_queryset(self):
        stname = self.kwargs['stname']
        print('jdkfjsfjfjdsfijsdfiojsdfiojifojdoifjdiofjdsoifjdiofjsdofjdiofjdoijfdiofjdsofjodfjdofjodjfsodfodjfoidsfodjfiodfiosdfo')
        print(stname)
        return Admin1Us.objects.filter(name__contains=stname)

    # print(name)
    bbox_filter_field = "wkb_geometry"
    filter_backends = (filters.InBBoxFilter,)

    serializer_class = worldserializer
