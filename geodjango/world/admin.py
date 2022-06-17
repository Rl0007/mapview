from django.contrib.gis import admin
from world.models import Admin1Us


# @admin.register(Admin1Us)
# class MarkerAdmin(admin.OSMGeoAdmin):
#     list_display = ("name", "wkb_geometry")

# Register your models here.
admin.site.register(Admin1Us, admin.GeoModelAdmin)
