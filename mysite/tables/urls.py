from django.urls import path
from tables import views

urlpatterns = [
    path('', views.ingresar_datos, name='Usuarios'),
    path('Ingresardatos/', views.ingresar_datos, name='ingresar datos'),
    path('success/', views.success_view, name='success'), 
]
