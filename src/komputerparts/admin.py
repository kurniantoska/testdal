# komputerparts/admin.py

from django.contrib import admin
from .models import (
    Monitor,
    Cpu,
    KomputerBuiltin
)

# Register your models here.
admin.site.register(Monitor)
admin.site.register(Cpu)
admin.site.register(KomputerBuiltin)

