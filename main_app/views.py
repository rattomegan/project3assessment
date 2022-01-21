from django.shortcuts import render
from .models import Widget

# Create your views here.
def widgets_index(request):
  widgets = Widget.objects.all
  return render(request, 'index.html', { 'widgets': widgets })