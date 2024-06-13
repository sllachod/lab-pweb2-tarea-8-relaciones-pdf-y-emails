from django.urls import path
from tables import views

urlpatterns = [
    path('datos/', views.ingresar_datos, name='ingresar_datos'),
    path('success/', views.success_view, name='success'), 
]
