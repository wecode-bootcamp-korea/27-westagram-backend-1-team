from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=45, verbose_name='이름')
    user_email = models.CharField(max_length=45, verbose_name='이메일')
    user_pwd = models.CharField(max_length=20, verbose_name='비밀번호')
    user_phone = models.CharField(max_length=20, verbose_name='전화번호')
    
    class Meta:
        db_table = 'users'