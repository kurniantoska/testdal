# komputerparts/views.py

from dal import autocomplete
from .models import Cpu

from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import KomputerBuiltinCreateForm 

# Create your views here.
class KomputerBuiltinCreateView(CreateView):
    form_class = KomputerBuiltinCreateForm
    template_name = 'form.html'

class CpuAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Cpu.objects.all()
        if self.q:
            qs = qs.filter(merk__istartswith=self.q)
        return qs
