from django.shortcuts import render
from .models import Widget
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.
def widgets_index(request):
  widgets = Widget.objects.all
  return render(request, 'index.html', { 'widgets': widgets })

class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'
  success_url = '/'

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'
