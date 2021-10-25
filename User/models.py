from ipaddress import AddressValueError

from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
class User(AbstractUser):
    username = None
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=100)

    USERNAME_FIELD= 'email'

    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.name

class Advisor(models.Model):
    name=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    advisor=models.ForeignKey(Advisor,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booking_time= models.DateTimeField(auto_now_add=True)