from django.db import models
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User,AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=10,unique=False) #bydefault usernname is unique
    contact = models.CharField('Contact',max_length=12,unique=True)
    first_name = models.CharField('first_name',max_length=30,blank=True)
    last_name = models.CharField('Last_name',max_length=30,blank=True)
    is_cleaner =models.BooleanField('cleaner',default=False)

    USERNAME_FIELD = 'contact'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.contact

    def get_firstname(self):
        return self.first_name


class City(models.Model):
    city_name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.city_name

class Cleaner(models.Model):
    user_id=models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)+str(self.city)

class Booking(models.Model):
    pass