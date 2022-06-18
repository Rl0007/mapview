import re
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from world.models import Admin1Us


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"

    # def dispatch(self, request, *args, **kwargs):
    #     self.name = kwargs.get('name', "any_default")

    # def dispatch(self, request, *args, **kwargs):
    #     self.name = kwargs.get('year', "any_default")


def mapview(request, param):
    return render(request, "map.html")


def show(request):

    showall = Admin1Us.objects.all()
    return render(request, "index.html", {'data': showall})


# class EditMushroomSpot(UpdateView):
#     model = Admin1Us
#     form_class = MushroomSpotForm
#     template_name = 'form.html'
