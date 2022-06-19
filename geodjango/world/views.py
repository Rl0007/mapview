import json
import re
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# Create your views here.
from django.views.generic.base import TemplateView
from world.models import Admin1Us
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import Polygon


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"


def mapview(request, param):
    return render(request, "map.html")


def show(request):

    showall = Admin1Us.objects.all()
    return render(request, "index.html", {'data': showall})


def add(request):
    return render(request, 'add.html')


def delete(request, id):
    val = id
    # print(val)
    todel = Admin1Us.objects.get(id=id).delete()

    return redirect('/show')


@csrf_exempt
def edit(request):
    data = request.POST.get('val')
    gjson = json.loads(data)
    id = gjson['properties']['id']
    coordinates = gjson['geometry']['coordinates'][0]
    editdata = Admin1Us.objects.get(id=id)
    display = editdata.wkb_geometry
    editdata.wkb_geometry = Polygon(coordinates)
    editdata.save()

    return render(request, "test.html")


@csrf_exempt
def create(request):
    data = request.POST.get('data')
    data = json.loads(data)
    print(data)
    coordinates = data['features'][0]['geometry']['coordinates'][0]
    coordinates = Polygon(coordinates)
    name = request.POST.get('name')
    country = request.POST.get('country')
    iso3166 = request.POST.get('iso3166')
    state_code = request.POST.get('state_code')
    id = request.POST.get('id')
    print(id)
    createdata = Admin1Us(name=name, country=country, iso3166_1_alpha_3=iso3166,
                          state_code=state_code, id=id, wkb_geometry=coordinates)

    createdata.save()
    print(coordinates)
    return redirect('/show')
