from django.shortcuts import render, redirect
from tables.form import NombreURLForm
from .models import NombreURL
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io

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
    return render(request, 'url/index.html', {'datos': datos})


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None

def pdf_view(request):
    datos = NombreURL.objects.all()
    context = {'datos': datos}
    pdf = render_to_pdf('url/index.html', context)
    
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="datos.pdf'
        return response
    return HttpResponse("Error al generar el PDF.", status=500)
