from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30,validators=[alphanumeric]);
    ph_num = models.IntegerField(null=False);
    
    # FOR UNQUE VALUES
    # unique=True 
    
    def __str__(self) :
        return self.name
    
class Msg(models.Model) :
    
    msg = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.msg
