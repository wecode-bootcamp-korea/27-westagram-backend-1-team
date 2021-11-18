from django.db import models

class User(models.Model) :
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45,unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    mbti = models.CharField(max_length=4, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'users'


