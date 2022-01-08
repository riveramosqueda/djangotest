from django.conf.urls import url,include
from django.urls import path
from apps.mascota.views import index,mascota_view

app_name = "mascota"

urlpatterns = [
    url(r'^$', index, name='index'),
    url('nuevo', mascota_view, name='nuevo'),
]