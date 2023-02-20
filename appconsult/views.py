from django.http import HttpResponse
from django.shortcuts import render
from appconsult.models import Professionals , Medical_Speciality, index
from appconsult.forms import ProfessionalsForm, Medical_specialityForm , indexForm
from django.views.generic import  DeleteView, ListView
from django.contrib.auth.decorators import login_required

def index(request):
     
 
   return render(request, 'index.html', context = {})

class imagelist(ListView):
      model = index
      template_name = "index.html"      
 
  
    
def add_prof(request): 
        
    if request.method =='GET':    
         context = {
         'form': ProfessionalsForm()
         }
         return render(request, 'add_prof.html', context=context)
    elif request.method == 'POST':   
         form = ProfessionalsForm(request.POST, request.FIlES)
         
         if form.is_valid():
                 Professionals.objects.create(
                 name=form.cleaned_data['name'],
                 speciality=form.cleaned_data["speciality"],
                 telehone=form.cleaned_data['telehone'], 
                 Email=form.cleaned_data['Email'],
                 picture=form.cleaned_data["picture"],
                 )
                 context = {
                  'message': 'Profesional ingresado exitosamente'
                  
                         }
                 
         return render(request, 'add_prof.html', context=context)
    else:
             context = {
            'form_errors': form.errors,
            'form': ProfessionalsForm()
              }
             return render(request, 'add_prof.html', context=context)



def list_prof(request):    
    if "search" in request.GET:  
      search = request.GET["search"]
      professional = Professionals.objects.filter(name__contains= search)     
    else:
        professional = Professionals.objects.all()
        
    context = {
        "Professionals":professional
    }
    return render(request,'list_prof.html', context = context) 

@login_required
def Professional_update(request, pk):
    professional = Professionals.objects.get(id=pk)
    if request.method == 'GET':
        context = {
            'form': ProfessionalsForm(  
                initial={
                    'name':professional.name,
                    'speciality':professional.speciality,
                    'telehone':professional.telehone,
                    'Email':professional.Email,
                    'picture':professional.picture,
                    
                    
                }   
            )
        }

        return render(request, 'professional_update.html', context=context)

    elif request.method == 'POST':
        form = ProfessionalsForm(request.POST, request.FILES)
        
        if form.is_valid():
            professional.name = form.cleaned_data['name']
            professional.speciality = form.cleaned_data['speciality']
            professional.telehone = form.cleaned_data['telehone']
            professional.Email = form.cleaned_data['Email']
            professional.picture = form.cleaned_data["picture"]
            
            professional.save()
            
            context = {
                'message': 'Profesional actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': ProfessionalsForm()
            }
        return render(request, 'professional_update.html', context=context)

class ProfessionalsDeleteView(DeleteView):
    model = Professionals
    template_name = 'professional_delete.html'
    success_url =  "/list_prof/"

def add_speciality(request):
    if request.method =='GET':    
         context = {
         'form':Medical_specialityForm()
         }
         return render(request, 'add_speciality.html', context=context)
    elif request.method == 'POST':   
         form = Medical_specialityForm(request.POST, request.FILES)
         if form.is_valid(): 
                 Medical_Speciality.objects.create(
                 Medical_Speciality=form.cleaned_data['Medical_Speciality'],
                 Description=form.cleaned_data["Description"], 
                 mspicture=form.cleaned_data["mspicture"],
                 )
                 context = {
                  'message': 'Especialidad ingresada exitosamente'
                         }
         return render(request, 'add_speciality.html', context=context)
    else:
             context = {
            'form_errors': form.errors,
            'form': Medical_specialityForm()
              }
             return render(request, 'add_speciality.html', context=context)

def list_speciality(request):
     if "buscar" in request.GET: 
          print(request.GET) 
          buscar = request.GET["buscar"]
          Speciality = Medical_Speciality.objects.filter(Medical_Speciality__contains= buscar)     
     else:
           Speciality = Medical_Speciality.objects.all()
     context = {
      "Medical_Speciality":Speciality
     }
     return render(request,'list_speciality.html', context = context) 

class SpecialityDeleteView(DeleteView):
      model = Medical_Speciality
      template_name = 'speciality_delete.html'
      success_url = "/list_speciality/"   

@login_required
def speciality_update(request, pk):
    
    Speciality = Medical_Speciality.objects.get(id=pk)
    print (request.GET)
    if request.method == 'GET':
        context = {
            'form': Medical_specialityForm(  
                initial={
                    'Medical_Speciality':Speciality.Medical_Speciality,
                    'Description':Speciality.Description,
                    'mspicture':Speciality.mspicture,
                    
                }   
            )
        }

        return render(request, 'speciality_update.html', context=context)

    elif request.method == 'POST':
        form = Medical_specialityForm(request.POST , request.FILES)
        if form.is_valid():
            Speciality.Medical_Speciality = form.cleaned_data['Medical_Speciality']
            Speciality.Description = form.cleaned_data['Description']
            Speciality.mspicture = form.cleaned_data['mspicture']
            
            
            Speciality.save()
            
            context = {
                'message': 'Especialidad actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': Medical_specialityForm()
            }
        return render(request, 'speciality_update.html', context=context)

def about_me (request):
    return render(request, 'about_me/about.html')               
            