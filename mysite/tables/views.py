from django.shortcuts import render, redirect
from tables.form import NombreURLForm
from .models import NombreURL

def ingresar_datos(request):
    if request.method == 'POST':
        form = NombreURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = NombreURLForm()
    
    return render(request, 'url/datos.html', {'form': form})

def success_view(request):
    return render(request, 'url/success.html')

def index(request):
    datos = NombreURL.objects.all()
    return render(request, 'index.html', {'datos': datos})