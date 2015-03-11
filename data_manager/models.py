from django.db import models
from boreholes.models import Drillhole, Well

# Create your models here.
class Duplicate(models.Model):
    table_id = models.IntegerField(null=True)
    table_name = models.TextField(null=True)
    entity_type = models.TextField(null=True)
    duplicate = models.ForeignKey("DuplicateType",null=True)

class DuplicateType(models.Model):
    kind = models.TextField(null=True)
    field = models.TextField(null=True)
    