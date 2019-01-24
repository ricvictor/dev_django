from django.urls import path
from . import views

app_name = 'GCacc'

urlpatterns = [
    path('', views.list_username, name='users'),
    path('new', views.new_user, name='new_user'),
    path('update/<int:id>/', views.update_user, name='update_user'),
    path('delete/<int:id>/', views.delete_user, name='delete_user'),
]
