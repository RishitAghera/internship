from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.
from django.db.models import Q
from django.http import HttpResponse, request
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import View,DetailView
from .models import BookingModel
from registration.models import Cleaner, City
from .forms import BookingForm, SLOT_CHOICE, BookingDetailForm


class BookingView(View):

    def get(self, request):
        form = BookingForm()
        return render(request, 'booking/booking_form.html', {'form': form})

    def post(self,request):
        form=BookingForm(data=request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            timeslot = form.cleaned_data.get('timeslot')
            date = form.cleaned_data.get('date')
            book = BookingModel.objects.filter(city__city_name=city, timeslot=timeslot, date=date)
            cleaner = Cleaner.objects.filter(city__city_name=city).exclude(
                user__in=[x.cleaner.user for x in book]).exclude(user=request.user)
            print(cleaner,city,date,timeslot)

            return render(request,'booking/booking_form.html',{'cleaner':cleaner,'city':city,'timeslot':timeslot,'date':date,'form':form})

class BookingList(DetailView):
    model=BookingModel
    template_name = 'booking/bookinglist.html'

    extra_context = {'form':BookingDetailForm()}




class BookingSave(View):

    @method_decorator(login_required, name='dispatch')
    def post(self,request):
        print(request.POST)
        data=request.POST.copy()
        city=City.objects.get(pk=data['city'])
        cleaner=Cleaner.objects.get(pk=data['cleaner'])
        o=BookingModel.objects.create(user=request.user,city=city,date=data['date'],cleaner=cleaner,timeslot=data['timeslot'])
        data=BookingModel.objects.filter(user=request.user)
        return render(request,'booking/postbooking.html')

