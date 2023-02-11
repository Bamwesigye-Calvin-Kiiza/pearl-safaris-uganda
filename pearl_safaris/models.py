from django.db import models

# Create your models here
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    
    def __str__(self):
        return self.first_name,self.last_name,self.email,self.phone_number