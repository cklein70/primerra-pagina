from django.db import models

class Medical_Studies(models.Model):
    name = models.CharField(max_length=50, verbose_name = "Nombre")
    Description = models.CharField(max_length=100,verbose_name = "Descripcion")
    preparation= models.CharField(max_length=200, verbose_name = "Preparacion previa")
    price=models.FloatField(verbose_name = "Precio")
    image = models.ImageField(upload_to ='Medical_studies_images', verbose_name="imagen" ,null=True, blank=True)
    
    class Meta:
        verbose_name="Estudio Medico "
        verbose_name_plural = "Estudios Medicos"

def __str__(self):
    return self.name - self. Descrition - self.price - self.image


       