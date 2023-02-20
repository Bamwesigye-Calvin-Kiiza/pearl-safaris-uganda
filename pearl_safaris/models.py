from django.db import models
from django.contrib.auth.models import User

# Create your models here
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    
    def __str__(self):
        return self.first_name,self.last_name,self.email,self.phone_number
    
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfoliosite = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures',blank=True)
    
    def __str__(self):
        return self.user.username