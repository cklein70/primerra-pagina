from django.contrib import admin
from Medical_studies.models import Medical_Studies

@admin.register(Medical_Studies)
class Medical_StudiesAdmin(admin.ModelAdmin):
     list_display = ("name", "Description");
     list_filter=("name", );
     search_fields = ("name",);
