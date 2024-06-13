from django import forms

class NombreURLForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    url = forms.URLField(label='URL')
