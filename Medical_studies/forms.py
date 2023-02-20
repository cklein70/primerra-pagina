from django import forms
from Medical_studies.models import Medical_Studies


    
class Medical_StudiesForms(forms.ModelForm):
        class Meta:
         model = Medical_Studies
         fields = ['name','Description','preparation','price','image']      