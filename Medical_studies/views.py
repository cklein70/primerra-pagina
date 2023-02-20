from django.views.generic import  CreateView, DeleteView 
from django.shortcuts import render
from Medical_studies.models import Medical_Studies
from Medical_studies.forms import Medical_StudiesForms
from django.contrib.auth.decorators import login_required


    
class StudiesCreateView(CreateView):
     model= Medical_Studies
     template_name="Medical_studies/studies_create.html"    
     fields= "__all__"
     success_url = "/Medical_studies/list_studies/"
     
     
def list_studies(request):    
    if "search" in request.GET:  
      search = request.GET ["search"]
      studies = Medical_Studies.objects.filter(name__contains= search)     
    else:
        
        studies = Medical_Studies.objects.all()
    
    context = {
        "Medical_Studies":studies
    }
    
    
    
    return render(request,'Medical_studies/studies_list.html', context = context)  
   
@login_required
def studies_update(request, pk):
    studies = Medical_Studies.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': Medical_StudiesForms(  
                 initial={
                    'name':studies.name,
                    'Description':studies.Description,
                    'preparation':studies.preparation,
                    'price':studies.price,
                    'image':studies.image,
                }   
            )
        }

        return render(request, 'Medical_studies/studies_update.html', context=context)

    elif request.method == 'POST':
        form = Medical_StudiesForms(request.POST, request.FILES )
        if form.is_valid():
            studies.name = form.cleaned_data['name']
            studies.Description = form.cleaned_data['Description']
            studies.preparation = form.cleaned_data['preparation']
            studies.price = form.cleaned_data['price']
            studies.image= form.cleaned_data["image"]
            
            studies.save()
            
            context = {
                'message': 'Estudio actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': Medical_StudiesForms()
            }
        return render(request, 'Medical_studies/studies_update.html', context=context)

class StudiesDeleteView(DeleteView):
    model = Medical_Studies
    template_name = 'Medical_studies/studies_delete.html'
    success_url = '/Medical_studies/list_studies/'