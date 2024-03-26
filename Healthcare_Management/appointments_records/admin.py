from django.contrib import admin
from .models import Patient, Appointment, MedicalRecord

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age','gender', 'email']

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date_time', 'reason']

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['patient']

admin.site.register(Patient,PatientAdmin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(MedicalRecord,MedicalRecordAdmin)
