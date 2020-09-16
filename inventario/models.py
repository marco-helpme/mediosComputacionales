from django.db import models

# Create your models here.



class Region(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Area(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class SO(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class PC(models.Model):
        area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, null=True)
        SO = models.ForeignKey(SO, on_delete=models.CASCADE, blank=True, null=True)
        numeroDeInventario = models.CharField(max_length=200)
        enRed = models.BooleanField(default=False)
        responsable = models.CharField(max_length=200, blank=True, null=True)

        def __str__(self):
            return str(self.numeroDeInventario + ' ' + self.area.nombre + ' ' + self.responsable)

class Cpu(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    capacidad = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.capacidad)

class Motherboard(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.noSerie)

class RAM(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    capacidad = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.capacidad) + ' ' + str(self.noSerie)

class HDD(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    capacidad = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.capacidad) + ' ' + str(self.noSerie)

class Monitor(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.noSerie)

class Impresora(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.noSerie)

class Teclado(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.noSerie)

class Mouse(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.noSerie)

class Bocinas(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.noSerie)

class UPS(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.noSerie)

class Estabilizador(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.noSerie)

class Targeta_de_Video(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    capacidad = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.capacidad) + ' ' + str(self.noSerie)

class Targeta_de_Red(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.noSerie)

class Fuente_Interna(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    capacidad = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.capacidad) + ' ' + str(self.noSerie)

class Lector(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    noSerie = models.CharField(max_length=200)
    def __str__(self):
        return self.marca + ' ' +  str(self.modelo) + ' ' + str(self.noSerie)



