from django.db import models

# Create your models here.

class Url(models.Model):
  shorturl = models.CharField(max_length=20, unique=True)
  fullurl = models.CharField(max_length=300)







