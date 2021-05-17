from django.contrib import admin
from .models import Information
from .forms import InformationForm

class InformationAdmin(admin.ModelAdmin) :
    model = Information
    form = InformationForm
    list_display = ('national_id', 'created', 'slug', 'pk')


admin.site.register(Information, InformationAdmin)