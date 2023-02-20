from django.db import models


class Professionals(models.Model):
    name = models.CharField(max_length=100, verbose_name = "nombre")
    speciality = models.CharField(max_length=40, verbose_name ="especialidad")
    telehone = models.CharField(max_length=10, verbose_name ="telefono")
    Email=models.EmailField()
    picture = models.ImageField(upload_to ='prof_images', verbose_name="imagen" ,null=True, blank=True)
    
    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
    
class Medical_Speciality(models.Model):
    Medical_Speciality= models.CharField (max_length = 40,verbose_name ="Especialidad medica")
    Description =models.CharField (max_length = 200,verbose_name ="Descripcion")
    mspicture = models.ImageField(upload_to ='medical_speciality_images', verbose_name="imagen" ,null=True, blank=True) 
    class Meta :
         verbose_name = "Especialidad Medica" 
         verbose_name_plural = "Especialidades Medicas"                                         
 
class index (models.Model):    
    image_index = models.ImageField(upload_to ='index_images',  blank=True,verbose_name = "imagenen index")
    
    class Meta:
        verbose_name="Imagen del Index "
        verbose_name_plural = "Imagenes del Index"
        
def __str__(self):
    return self.inage_index 
