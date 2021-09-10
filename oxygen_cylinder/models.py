from django.db import models
# Create your models here.
class Cylinder_Request(models.Model):   
    """
        This Cylinder_Request class is extended from the model class. 

        So, it has all the functionality of the model class.

        Attributes: pID, pName, firstName, lastName, email, contactNum, address, city, postalCode

        Functions: This class requires no functions.

        This class is used to create objects for database entry of oxygen cylinder requests.
    """
    pID = models.CharField(max_length=50)
    pName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contactNum = models.CharField(max_length=14) 
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=15)
    postalCode = models.CharField(max_length=10)
