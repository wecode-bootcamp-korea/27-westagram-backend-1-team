from django.db import models

# Create your models here.

class User(models.Model):
    # 유저 이름(실명)
    name     = models.CharField(max_length=15)
    # 유저 이메일(고유값)
    email    = models.CharField(max_length=254 , unique=True)
    # 유저 비밀번호
    password = models.CharField(max_length=45)
    # 유저 휴대전화 번호(고유값)
    contact  = models.CharField(max_length=11  , unique=True)
    # 유저 mbti(null 가능)
    mbti     = models.CharField(max_length=4   , null=True)
    # 유저 성별(기본 = 'U'nknown)
    gender   = models.CharField(max_length=1   , default='U')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
