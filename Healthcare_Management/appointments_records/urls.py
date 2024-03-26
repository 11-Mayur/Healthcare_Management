from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('patients/', views.PatientListCreate.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientRetrieveUpdateDestroy.as_view(), name='patient-retrieve-update-destroy'),
    path('appointments/', views.AppointmentListCreate.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', views.AppointmentRetrieveUpdateDestroy.as_view(), name='appointment-retrieve-update-destroy'),
    path('records/', views.MedicalRecordListCreate.as_view(), name='medical-record-list-create'),
    path('records/<int:pk>/', views.MedicalRecordRetrieveUpdateDestroy.as_view(), name='medical-record-retrieve-update-destroy'),
    path('logout/', views.Logout),
]




