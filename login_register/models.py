from django.db import models


# Create your models here.
class LogIn(models.Model):
    """
    This LogIn class is extended from the Model class 
    so it has all the functionality of the model class.

    Attributes: userEmail, userPassword.

    Functions: This LogIn class requires no functions.

    This LogIn class used to create objects for database entry.
    """
    userEmail = models.EmailField(max_length=50)
    userPassword = models.CharField(max_length=50)


class UserSignUp(models.Model):
    """
    This UserSignUp class is extended from the Model class 
    so it has all the functionality of the model class.

    Attributes: userFname, userLname, userAge, userDob,  
    userGender, userOccupation, userCnumber, userBgroup, 
    userEmail, userPassword, userCPassword.

    Functions: This UserSignUp class requires no functions.

    This UserSignUp class used to create objects for database entry.
    """
    userFname = models.CharField(max_length=50)
    userLname = models.CharField(max_length=50)
    userAge = models.IntegerField()
    userDob = models.DateField(auto_now=False, auto_now_add=False)
    userGender = models.CharField(max_length=10)
    userOccupation = models.CharField(max_length=30)
    userCnumber = models.CharField(max_length=30)
    userBgroup = models.CharField(max_length=20)
    userEmail = models.EmailField(max_length=50)
    userPassword = models.CharField(max_length=50)
    userCPassword = models.CharField(max_length=50)



    
