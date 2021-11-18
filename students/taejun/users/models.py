from django.db import models

# Create your models here.

class User(models.Model):
    name     = models.CharField(max_length=15)
    email    = models.CharField(max_length=254 , unique=True)
    password = models.CharField(max_length=45)
    contact  = models.CharField(max_length=11  , unique=True)
    mbti     = models.CharField(max_length=4   , null=True)
    gender   = models.CharField(max_length=1   , default='U')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
