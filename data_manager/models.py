from django.db import models

# Create your models here.
class Duplicate(models.Model):
    table_id = models.IntegerField(null=True)
    table_name = models.TextField(null=True)
    entity_type = models.TextField(null=True)
    duplicate_group = models.ForeignKey("DuplicateGroup",null=True)

class DuplicateGroup(models.Model):
    kind = models.TextField(null=True)
    field = models.TextField(null=True)
    