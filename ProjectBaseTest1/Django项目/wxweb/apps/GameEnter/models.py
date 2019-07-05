from django.db import models

# Create your models here.

class SingUp(models.Model):
    ID = models.IntegerField(primary_key=True, auto_created=True, verbose_name='自增ID')
    Guid = models.CharField(max_length=32, verbose_name='唯一ID')
    UserName = models.CharField(max_length=20, blank=False, verbase_name='用户名')