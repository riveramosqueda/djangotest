from django.conf.urls import url,include
from django.urls import path
from apps.mascota.views import MascotaList,MascotaCreate,MascotaUpdate,MascotaDelete

app_name = "mascota"

urlpatterns = [
    url(r'^$', MascotaList.as_view(), name='index'),
    url(r'crear', MascotaCreate.as_view(), name='crear'),
    url(r'editar/(?P<pk>\d+)$', MascotaUpdate.as_view(), name='editar'),
    url(r'eliminar/(?P<pk>\d+)$', MascotaDelete.as_view(), name='eliminar'),
]