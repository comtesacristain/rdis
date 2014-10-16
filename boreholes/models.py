from django.db import models

# Create your models here.

class Deposit(models.Model):
    eno = models.AutoField(primary_key=True)
    
    class Meta:
<<<<<<< HEAD
        db_table = '"mgd"."deposits"'
=======
        db_table = 'mgd.deposits'


class Borehole(models.Model):
    eno = models.AutoField(primary_key=True)
    
    class Meta:
        db_table = 'a.entities'
>>>>>>> 7f765c0ad062cb2e08e52a66b079244a0cf15939
