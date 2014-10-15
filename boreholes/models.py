from django.db import models

# Create your models here.

class Deposit(models.Model):
eno = models.AutoField(primary_key=True)
    
    class Meta:
        db_table = 'mgd.deposits'
