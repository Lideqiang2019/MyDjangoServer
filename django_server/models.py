# from django.db import models
from django.contrib.gis.db import models

# Create your models here.

# class Land1029(models.Model):
#     gid = models.IntegerField(blank=True, primary_key=True)
#     objectid_1 = models.BigIntegerField(blank=True, null=True)
#     objectid_2 = models.BigIntegerField(blank=True, null=True)
#     objectid = models.BigIntegerField(blank=True, null=True)
#     block_name = models.CharField(max_length=100,blank=True,null=True)
#     block_use = models.CharField(max_length=50,blank=True,null=True)
#     block_area = models.DecimalField(max_digits=15, decimal_places=6)
#     block_leng = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
#     floor_area = models.DecimalField(max_digits=15, decimal_places=6)
#     arc_area = models.FloatField()
#     density = models.FloatField()
#     far = models.DecimalField(max_digits=15, decimal_places=6)
#     shape_idx = models.FloatField()
#     shape_leng = models.DecimalField(max_digits=15, decimal_places=6)
#     shape_le_1 = models.DecimalField(max_digits=15, decimal_places=6)
#     shape_area = models.DecimalField(max_digits=15, decimal_places=6)
#     geom = models.PolygonField()
#     # geom = models.GeometryField(blank=True, null=True)

# class Meta:
#     managed = False
#     db_table = 'land1029'
class Land1029(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    objectid_2 = models.BigIntegerField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    block_name = models.CharField(max_length=100, blank=True, null=True)
    block_use = models.CharField(max_length=50, blank=True, null=True)
    block_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    block_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    floor_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    arc_area = models.FloatField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    far = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_idx = models.FloatField(blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_le_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'land1029'

# class DjangoServerLand1029(models.Model):
#     gid = models.IntegerField(primary_key=True)
#     block_name = models.CharField(max_length=50, blank=True, null=True)
#     block_area = models.DecimalField(max_digits=15, decimal_places=6)
#     floor_area = models.DecimalField(max_digits=15, decimal_places=6)
#     arc_area = models.FloatField()
#     density = models.FloatField()
#     far = models.DecimalField(max_digits=15, decimal_places=6)
#     shape_idx = models.FloatField()
#     shape_leng = models.DecimalField(max_digits=15, decimal_places=6)
#     shape_le_1 = models.DecimalField(max_digits=15, decimal_places=6)
#     shape_area = models.DecimalField(max_digits=15, decimal_places=6)
#     geom = models.GeometryField()

#     class Meta:
#         managed = False
#         db_table = 'django_server_land1029'
