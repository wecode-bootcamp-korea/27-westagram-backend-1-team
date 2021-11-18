from django.db import models

class User(models.Model) :
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45,unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    mbti = models.CharField(max_length=4, null=True)

    class Meta:
        db_table = 'users'


