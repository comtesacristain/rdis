from django.contrib.gis.db import models

# Create your models here.

class Entity(models.Model):
    eno = models.AutoField(primary_key=True)
    entityid = models.TextField()
    entity_type = models.TextField()
    entrydate = models.DateField(null=True)
    access_code = models.TextField(null=True)
    geom = models.GeometryField(srid=8311,null=True)
    objects = models.GeoManager()
	
    def __str__(self):              # __unicode__ on Python 2
        return self.entityid
	
    class Meta:
        db_table = '"a"."entities"'
        #abstract = True

class EntitiesManager(models.GeoManager):
    def __init__(self,entity_type):
        super(EntitiesManager, self).__init__()
        
        self.entity_type=entity_type

    def get_queryset(self):
        return super(EntitiesManager, self).get_queryset().filter(entity_type=self.entity_type)

#class Drillhole(Entity):
#   objects=EntitiesManager("DRILLHOLE")
	
class Well(models.Model):
    #eno = models.AutoField(primary_key=True)
    welltype = models.TextField()    
    purpose = models.TextField()
    classification = models.TextField()
    operator = models.TextField()
    status = models.TextField()
    start_date = models.DateField()
    completion_date = models.DateField()
    total_depth =models.IntegerField()
    orig = models.TextField(db_column="originator")
    origno = models.ForeignKey("Originator",db_column="origno",null=True)
    
    def originator(self):
        if self.origno is None:
            return self.orig
        else:
            return self.origno.originator
            
    
	
    entity = models.OneToOneField("Entity",primary_key=True,db_column="eno")
    class Meta:
        db_table = '"npm"."wells"'

        
class Originator(models.Model):
    origno =  models.AutoField(primary_key=True)
    originator = models.TextField()
    class Meta:
        db_table = '"a"."v_originators"'
#class Well(Entity):
#    objects=EntitiesManager("WELL")
	
#class Deposit(Entity):
#    objects=EntitiesManager("MINERAL DEPOSIT")
 

#class Province(Entity):
#    objects=EntitiesManager("PROVINCE") 
    
#class Survey(Entity):
#    objects=EntitiesManager("SURVEY")
        
class Sample(models.Model):
    sampleno = models.AutoField(primary_key=True)
    sampleid = models.TextField()
    entity = models.ForeignKey("Entity",db_column="eno")
    
    def __str__(self):              # __unicode__ on Python 2
        return self.sampleid
    
    class Meta:
        db_table = '"a"."samples"'
        
class SampleData(models.Model):
    datano = models.AutoField(primary_key=True)
    sample = models.ForeignKey("Sample",db_column="sampleno")

    
    class Meta:
        db_table = '"a"."sampledata"'
