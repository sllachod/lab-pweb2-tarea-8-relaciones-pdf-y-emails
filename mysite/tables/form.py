from django import forms
from .models import NombreURL

class NombreURLForm(forms.ModelForm):
    class Meta:
        model = NombreURL
        fields = ['nombre', 'url']
    
class EmailForm(forms.Form):
    destinatario = forms.EmailField(label='Correo electrónico del destinatario')
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea)
