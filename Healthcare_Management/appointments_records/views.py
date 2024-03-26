from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from .models import Patient, Appointment, MedicalRecord
from .serializers import PatientSerializer, AppointmentSerializer, MedicalRecordSerializer

@login_required
def Index(request):
    return render(request, 'appointments_records/index.html')

def Logout(r):
    return render(r,'appointments_records/logout.html')

class PatientListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class PatientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class AppointmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class MedicalRecordListCreate(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]

class MedicalRecordRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]




