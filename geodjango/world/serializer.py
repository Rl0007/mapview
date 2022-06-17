
from rest_framework_gis import serializers

from world.models import Admin1Us as table


class worldserializer(serializers.GeoFeatureModelSerializer):
    """Marker GeoJSON serializer."""

    class Meta:
        """Marker serializer meta class."""

        fields = ("id", "name")
        geo_field = "wkb_geometry"
        model = table
