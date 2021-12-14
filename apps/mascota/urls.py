from django.conf.urls import url,include
from django.urls import path
from apps.mascota.views import index

app_name = "mascota"

urlpatterns = [
    url('', index, name='index'),
]