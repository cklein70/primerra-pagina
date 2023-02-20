"""consultorio1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from appconsult import views  
from appconsult.views import  add_prof, list_prof, index, add_speciality, list_speciality ,SpecialityDeleteView, speciality_update, Professional_update, ProfessionalsDeleteView, about_me
from django.conf.urls.static import static
from django.conf import settings
from consultorio1.settings import MEDIA_ROOT, MEDIA_URL
urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('add_prof/', add_prof),
    path('list_prof/', list_prof),
    path ("add_speciality/",add_speciality),
    path ("list_speciality/",list_speciality),
    path("Medical_studies/", include ("Medical_studies.urls")),
    path("speciality_delete/<int:pk>/", SpecialityDeleteView.as_view(), name= "speciality_detete"),
    path("speciality_update/<int:pk>/", speciality_update),
    path("professional_update/<int:pk>/", Professional_update),
    path("professional_delete/<int:pk>/", ProfessionalsDeleteView.as_view(), name= "professional_detete"),
    path('user/', include('user.urls')),
    path('about/', about_me, name='about_me'),
     ] + static(MEDIA_URL, document_root = MEDIA_ROOT)  

