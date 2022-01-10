from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascota.models import Mascota
from apps.mascota.forms import MascotaForm

# Create your views here.
def index(request):
  mascotas=Mascota.objects.all().order_by('-id')
  contexto={'mascotas':mascotas}

  return render(request, 'mascota/index.html', contexto)

def mascota_crear(request):
  if request.method=='POST':
    form=MascotaForm(request.POST)
    if form.is_valid:
      form.save()
    return redirect('mascota:index')
  else:
    form=MascotaForm()
  
  return render(request, 'mascota/form.html', {'form':form})

def mascota_editar(request, id):
  mascota=Mascota.objects.get(id=id)
  if request.method=='GET':
    form=MascotaForm(instance=mascota)
  else:
    form=MascotaForm(request.POST,instance=mascota)
    if form.is_valid():
      form.save()
    return redirect('mascota:index')

  return render(request, 'mascota/form.html', {'form':form})

def mascota_eliminar(request):
  mascota=Mascota.objects.get(id=request.POST['delete_id'])
  if request.method=='POST' and mascota:
    mascota.delete()
  return redirect('mascota:index')