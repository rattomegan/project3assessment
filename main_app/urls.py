from django.urls import path
from . import views


urlpatterns = [
  path('', views.widgets_index, name='widgets_index')
]