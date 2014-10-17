from django.contrib.gis.db import models

# Create your models here.

class Deposit(models.Model):
    eno = models.AutoField(primary_key=True)
    
    class Meta:
        db_table = '"mgd"."deposits"'


class Borehole(models.Model):
    eno = models.AutoField(primary_key=True)
    entityid = models.TextField()
    entity_type = models.TextField()
    
    geom = models.GeometryCollectionField()
    objects=models.GeoManager()    
 
    def __str__(self):              # __unicode__ on Python 2
        return self.entityid
    
    class Meta:
        db_table = '"a"."entities"'
        
