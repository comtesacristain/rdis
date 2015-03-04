from django.contrib.gis.db import models

# Create your models here.

class Entity(models.Model):
    eno = models.AutoField(primary_key=True)
    entityid = models.TextField()
    entity_type = models.TextField()
    confid_until = models.DateField()
    access_code = models.TextField()
    geom = models.GeometryField(srid=8311)

    def __str__(self):              # __unicode__ on Python 2
        return self.entityid
	
    class Meta:
        db_table = '"a"."entities"'
        abstract = True

class EntitiesManager(models.GeoManager):
    def __init__(self,entity_type):
        super(EntitiesManager, self).__init__()
        self.entity_type=entity_type

    def get_queryset(self):
        return super(EntitiesManager, self).get_queryset().filter(entity_type=self.entity_type)

class BoreholesManager(models.GeoManager):
    def get_queryset(self):
        return super(BoreholesManager, self).get_queryset().filter(entity_type="DRILLHOLE")

class Borehole(Entity):
    objects=BoreholesManager()
 
class Deposit(Entity):
    objects=EntitiesManager("MINERAL DEPOSIT")
 
class Province(Entity):
    objects=EntitiesManager("PROVINCE") 
    
class Survey(Entity):
    objects=EntitiesManager("SURVEY")
        
class Sample(models.Model):
    sampleno = models.AutoField(primary_key=True)
    entity = models.ForeignKey("Entity",db_column="eno")
    
    class Meta:
        db_table = '"a"."samples"'
    pass