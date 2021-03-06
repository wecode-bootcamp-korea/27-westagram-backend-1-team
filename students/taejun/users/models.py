from django.db import models

class User(models.Model):
    name       = models.CharField(max_length=15)
    email      = models.CharField(max_length=254, unique=True)
    password   = models.CharField(max_length=200)
    contact    = models.CharField(max_length=50, unique=True)
    mbti       = models.CharField(max_length=4, blank=True)
    gender     = models.CharField(max_length=9, default='Undefined')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
