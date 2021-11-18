from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length = 255, unique=True)
    password = models.CharField(max_length = 128)
    phone = models.CharField(max_length = 15)
    introduce = models.CharField(max_length=150)

    class Meta:
        db_table = 'users'

"""
User class 생성
이름, 이메일, 비밀번호, 폰, 개인소개
"""
