from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import render, redirect
from apps.mascota.models import Mascota
from apps.mascota.forms import MascotaForm

# Create your views here.
class MascotaList(ListView):
  model=Mascota
  template_name='mascota/index.html'

class MascotaCreate(CreateView):
  model=Mascota
  form_class=MascotaForm
  template_name='mascota/form.html'
  success_url=reverse_lazy('mascota:index')

class MascotaUpdate(UpdateView):
  model=Mascota
  form_class=MascotaForm
  template_name='mascota/form.html'
  success_url=reverse_lazy('mascota:index')

class MascotaDelete(DeleteView):
  model=Mascota
  success_url=reverse_lazy('mascota:index')