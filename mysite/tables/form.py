from django import forms
from .models import NombreURL

class NombreURLForm(forms.ModelForm):
    class Meta:
        model = NombreURL
        fields = ['nombre', 'url']
