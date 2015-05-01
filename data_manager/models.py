from django.db import models
from boreholes.models import Entity

# Create your models here.
class Duplicate(models.Model):
    eno = models.IntegerField(null=True)
    table_name = models.TextField(null=True)
    entity_type = models.TextField(null=True)
    entityid = models.TextField(null=True)
    duplicate_group = models.ForeignKey("DuplicateGroup",null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    z = models.FloatField(null=True)
    has_well = models.BooleanField(default=False)
    has_samples = models.BooleanField(default=False)
    no_samples = models.IntegerField(null=True)
    
    action_status = models.TextField(default='UN')
    deleted = models.TextField(default='N')
    data_transferred_to = models.IntegerField(null=True)
    
    def __str__(self):
        return "{0}: {1}".format(self.eno,self.entityid)
        
    def entity(self):
        return Entity.objects.get(pk=self.eno)
    
class DuplicateGroup(models.Model):
    kind = models.TextField(null=True)
    field = models.TextField(null=True)
    num_dupes = models.IntegerField(null=True)
    has_resolution = models.TextField(default='N')
    qaed = models.TextField(default='N')
    
    def number_of_wells(self):
        return self.duplicate_set.filter(entity_type='WELL').count()
        
    def number_of_drillholes(self):
        return self.duplicate_set.filter(entity_type='DRILLHOLE').count()
    
    def __str__(self):
        return "{0}: {1}".format(self.id,self.kind)