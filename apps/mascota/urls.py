from django.conf.urls import url,include
from django.urls import path
from apps.mascota.views import index,mascota_crear,mascota_editar,mascota_eliminar

app_name = "mascota"

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'crear', mascota_crear, name='crear'),
    url(r'editar/(?P<id>\d+)$', mascota_editar, name='editar'),
    url(r'eliminar$', mascota_eliminar, name='eliminar'),
]