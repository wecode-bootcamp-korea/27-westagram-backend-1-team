from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length = 255, unique=True)
    password = models.CharField(max_length = 128)
    phone = models.CharField(max_length = 15)
    introduce = models.CharField(max_length=150)

    class Meta:
        db_table = 'users'