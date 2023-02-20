from django import forms
from appconsult.models import Professionals , Medical_Speciality ,index
   
    

       
class Medical_specialityForm(forms.ModelForm):
       class Meta:
         model = Medical_Speciality
         fields = ['Medical_Speciality','Description','mspicture']
                
            
class indexForm(forms.ModelForm):
    class Meta:
       model = index
       fields = ('image_index',)
       
class ProfessionalsForm(forms.ModelForm):
     class Meta:
        model = Professionals
        fields = ['name','speciality','telehone','Email','picture']      