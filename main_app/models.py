from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class Widget(models.Model):
  description = models.CharField(max_length=100)
  quantity = models.IntegerField(default=0)

  def __str__(self):
    return self.description