from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """
     This class is extended from the model class. So, it has all the functionality of model class.

     This class is used to create objects fro database entry.
    """
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    post = models.CharField(max_length=100000)