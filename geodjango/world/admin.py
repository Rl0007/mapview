from django.contrib.gis import admin
from world.models import Admin1Us
# from leaflet.admin import leafletGeoAdmin

# from leaflet.admin import LeafletGeoAdmin
# @admin.register(Admin1Us)
# class MarkerAdmin(admin.OSMGeoAdmin):
#     list_display = ("name", "wkb_geometry")

# Register your models here.
admin.site.register(Admin1Us, admin.GeoModelAdmin)
# admin.site.register(Admin1Us, leafletGeoAdmin )
# admin.site.register(Admin1Us, LeafletGeoAdmin)
