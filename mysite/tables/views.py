from django.shortcuts import render, redirect
from tables.form import NombreURLForm

def ingresar_datos(request):
    if request.method == 'POST':
        form = NombreURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = NombreURLForm()
    
    return render(request, 'pdf/datos.html', {'form': form})

def success_view(request):
    return render(request, 'pdf/success.html')
