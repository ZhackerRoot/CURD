from django.db import models

# Create your models here.
class Student(models.Model):  
    firstname = models.CharField(max_length=50)  
    lastname  = models.CharField(max_length = 10)  
    email     = models.EmailField()  
    file      = models.FileField() # for creating file input  
    class Meta:
        db_table = 'student'