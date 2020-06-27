from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#creating a customer user model CharacterView
#this can be changed in the future, just making basic user profile for now

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
