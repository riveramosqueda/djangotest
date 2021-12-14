from django.conf.urls import url,include
from django.urls import path
from apps.adopcion.views import index

app_name = "adopcion"

urlpatterns = [
    url('', index, name='index'),
]