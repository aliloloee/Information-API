from django.contrib import admin
from .models import Information, ECGInformation

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin) :
    model = Information
    list_display = ('national_id', 'fullname', 'pk')
    readonly_fields = ('slug', )


@admin.register(ECGInformation)
class ECGInformationAdmin(admin.ModelAdmin) :
    list_display = ('get_patient_national_id', 'get_patient_name', )
    search_fields = ('patient__fullname', 'patient__national_id', 'doctor__fullname', )
    readonly_fields = ('recorded_at', 'slug', )
    # * searching for : patient name, doctor name, patient national id, 

    @admin.display(description='NATIONAL ID')
    def get_patient_national_id(self, obj) :
        return f'{obj.patient.national_id}'

    @admin.display(description='FULLNAME')
    def get_patient_name(self, obj) :
        return f'{obj.patient.fullname}'
