from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascota.models import Mascota
from apps.mascota.forms import MascotaForm

# Create your views here.
def index(request):
  mascotas=Mascota.objects.all()
  contexto={'mascotas':mascotas}
  return render(request, 'mascota/index.html', contexto)
  #return render(request,'mascota/index.html')

def mascota_view(request):
  if request.method=='POST':
    form=MascotaForm(request.POST)
    if form.is_valid:
      form.save()
    return redirect('mascota:index')
  else:
    form=MascotaForm()
  
  return render(request, 'mascota/form.html', {'form':form})