from django.db import models

class User(models.Model):
    name    = models.CharField(max_length=45)
    email   = models.CharField(max_length=45)
    pwd     = models.CharField(max_length=20)
    phone   = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'users'
