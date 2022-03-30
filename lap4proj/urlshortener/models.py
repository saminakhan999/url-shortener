from django.db import models

# Create your models here.

class Url(models.Model):
  shorturl = models.CharField(max_length=20)
  fullurl = models.CharField(max_length=300)



