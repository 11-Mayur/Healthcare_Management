from django.db import models

# Create your models here.

class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    contact = models.BigIntegerField(default=0)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return "Appointment for {} at {}".format(self.patient,self.date_time)


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # Add fields for medical records
    # Example: condition, diagnosis, medication, etc.

    def __str__(self):
        return f"Medical record for {self.patient}"



