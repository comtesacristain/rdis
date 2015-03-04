from django.db import models

# Create your models here.
class Duplicate(models.Model):
    table_id = models.IntegerField()
    table_name = models.TextField()
    duplicate = models.ForeignKey("DuplicateType")

class DuplicateType(models.Model):
    kind = models.TextField()
    field = models.TextField()
    model = models.TextField()
    