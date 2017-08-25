from django.db import models

# Create your models here.
class Monitor(models.Model):
    merk            = models.CharField(max_length=120)
    tahun_pembuatan = models.CharField(max_length=4)
    harga           = models.CharField(max_length=10)

    def __str__(self):
        return self.merk

class Cpu(models.Model):
    merk            = models.CharField(max_length=120)
    fitur           = models.CharField(max_length=100)
    harga           = models.CharField(max_length=10)

    def __str__(self):
        return self.merk

class KomputerBuiltin(models.Model):
    nama_paket      = models.CharField(max_length=120)
    monitor         = models.ForeignKey(Monitor)
    cpu             = models.ForeignKey(Cpu)

    def __str__(self):
        return self.nama_paket
