from django.urls import path 
from Medical_studies.views import  StudiesCreateView , list_studies, studies_update, StudiesDeleteView #StudiesListView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
  # path ("studies_list/", StudiesListView.as_view(), name= "studies_list" ),
   path ("studies_create/", StudiesCreateView.as_view(), name= "studies_create" ),
   path ("list_studies/", list_studies),
   path("studies_update/<int:pk>/", studies_update, name= "studies_update"),
   path("studies_delete/<int:pk>/", StudiesDeleteView.as_view(), name= "studies_detete"),
  
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)