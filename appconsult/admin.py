from django.contrib import admin

from appconsult.models import  Professionals , Medical_Speciality, index

#admin.site.register (Professionals)
@admin.register(Professionals)
class ProfesssionalsAdmin(admin.ModelAdmin):
     list_display = ("name", "speciality");
     list_filter=("name", "speciality");
     search_fields = ("name", "speciality");
     
     
@admin.register(Medical_Speciality)
class Medical_SpecialityAdmin(admin.ModelAdmin):
     list_display = ("Medical_Speciality", "Description");    
     
@admin.register(index)
class indexAdmin(admin.ModelAdmin):
     list_display = ("image_index",);   