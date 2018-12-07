from django.urls import path
from . import views

app_name = 'GCacc'

urlpatterns = [
    path('', views.index, name='index'),
    path('teste', views.home, name='teste'),
]
