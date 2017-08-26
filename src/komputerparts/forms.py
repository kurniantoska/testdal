# komputerparts/forms.py

from dal import autocomplete 

from django import forms
from .models import KomputerBuiltin

class KomputerBuiltinCreateForm(forms.ModelForm):
    class Meta:
        model = KomputerBuiltin
        fields = ('__all__')
        widgets = {
            'cpu':autocomplete.ModelSelect2(url='api-get-cpu')
        }
