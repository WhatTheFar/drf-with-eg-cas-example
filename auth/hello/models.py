from django.db import models


# Create your models here.

class Auth(models.Model):
    name = models.name = models.CharField(max_length=255, verbose_name="Name")

    class Meta:
        verbose_name = 'Auth'
