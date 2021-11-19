from django.db import models

class User(models.Model):
    name     = models.CharField(max_length=30)
    email    = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    phone    = models.CharField(max_length=15)
    bio      = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
