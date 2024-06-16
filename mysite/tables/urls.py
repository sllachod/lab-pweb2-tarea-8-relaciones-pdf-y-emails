from django.urls import path
from tables import views

urlpatterns = [
    path('', views.index, name='Usuarios'),
    path('Ingresardatos/', views.ingresar_datos, name='ingresar datos'),
    path('success/', views.success_view, name='success'),
    path('pdf/', views.pdf_view, name='pdf_view'),
    path('enviar_mail/', views.enviar_email, name='enviar_email'),
    path('email_enviado/', views.success_view, name='email_success'),
]
