

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name ='profile')
    phone = models.CharField(max_length=25, null=True, blank=True, verbose_name ="telefono")
    birth_date = models.DateField(null=True, blank=True , verbose_name ="fecha de nacimiento")
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)

    class Meta:
        verbose_name="Perfil de usuario "
        verbose_name_plural = "Perfiles de usuarios"