# from django.db import models
from django.contrib.gis.db import models
# from django.db.models import Manager as GeoManager
# Create your models here.
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):

    operations = [
        CreateExtension('postgis'),
        ...
    ]


class Admin1Us(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    iso3166_1_alpha_3 = models.CharField(max_length=10, blank=True, null=True)
    state_code = models.CharField(max_length=10, blank=True, null=True)
    id = models.CharField(max_length=15, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin1_us'
