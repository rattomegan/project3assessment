from django.urls import path
from . import views


urlpatterns = [
  path('', views.widgets_index, name='widgets_index'),
  path('addwidget/', views.WidgetCreate.as_view(), name='add_widget'),
  path('deletewidget/<int:pk>/delete/', views.WidgetDelete.as_view(), name='delete_widget'),
]