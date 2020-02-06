from django.db import models
from django.urls import reverse

from registration.models import User,Cleaner,City
# Create your models here.


class BookingModel(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    cleaner=models.ForeignKey(Cleaner,null=True,on_delete=models.SET_NULL)
    date=models.DateField()
    city=models.ForeignKey(City,null=True,on_delete=models.SET_NULL)
    timeslot=models.IntegerField(null=True)

    def __str__(self):
        return self.cleaner.user.first_name+' '+str(self.city)

    def get_absolute_url(self):
        return reverse('booking:bookinglist',kwargs={'pk':self.pk})