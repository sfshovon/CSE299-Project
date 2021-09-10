from django.db import models

# Create your models here.
class Appointment(models.Model):
    """
     This class is extended from the model class. So, it has all the functionality of model class.

     This class is used to create objects fro database entry.
    """
    date = models.DateField(auto_now=False, auto_now_add=False)
    timeSlot = models.TimeField(auto_now=False, auto_now_add=False)
    doctorId = models.CharField(max_length=100)
    patientId = models.CharField(max_length=100)