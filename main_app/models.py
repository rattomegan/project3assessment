from django.db import models
from django.urls import reverse

# Create your models here.
class Widget(models.Model):
  description = models.CharField(max_length=100)
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return self.description

  def get_absolute_url(self):
    return reverse('widgets_index')