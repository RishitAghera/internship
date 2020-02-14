from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, send_mass_mail
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import View, DetailView, DeleteView
from mysql.connector import connect

from Homework.settings import EMAIL_HOST_USER
from .models import BookingModel
from registration.models import Cleaner, City
from .forms import BookingForm, BookingDetailForm


class BookingView(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        form = BookingForm()
        return render(request, 'booking/booking_form.html', {'form': form})

    @method_decorator(login_required, name='dispatch')
    def post(self,request):
        form=BookingForm(data=request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            timeslot = form.cleaned_data.get('timeslot')
            date = form.cleaned_data.get('date')
            book = BookingModel.objects.filter(city__city_name=city, timeslot=timeslot, date=date)
            cleaner = Cleaner.objects.filter(city__city_name=city).exclude(
                user__in=[x.cleaner.user for x in book]).exclude(user=request.user)
            return render(request,'booking/booking_form.html',{'cleaner':cleaner,'city':city,'timeslot':timeslot,'date':date,'form':form,'star_counter':range(5)})

class BookingDetail(DetailView):
    model=BookingModel
    template_name = 'booking/bookingdetail.html'

    extra_context = {'form':BookingDetailForm()}

class DeleteBooking(DeleteView):
    model=BookingModel
    # template_name = 'booking/bookingmodel_confirm_delete.html'
    success_url = reverse_lazy('booking:mybookinglist')



class BookingSave(View):

    @method_decorator(login_required, name='dispatch')
    def post(self,request):
        data=request.POST.copy()
        city=City.objects.get(pk=data['city'])
        print(city.city_name)
        cleaner=Cleaner.objects.get(pk=data['cleaner'])
        print(cleaner.user.first_name)
        print(data['date'])
        o=BookingModel.objects.create(user=request.user,city=city,date=data['date'],cleaner=cleaner,timeslot=data['timeslot'])
        # recepient=(Cleaner.objects.get(pk=data['cleaner']).user.email)
        #
        # cleaner_msg = "You have Book for a Date:" + data['date'] + " for cleaning service at " + city.city_name + "\nCustomer name : " + cleaner.user.first_name + "\nSee Your Orders List :127.0.0.1:8000/bookorder/'"
        #
        # customer_msg = "You have Book for a Date:" + data['date'] + " for cleaning service at " + city.city_name + "\nCustomer name : " + cleaner.user.first_name + "\nSee Your Orders List :127.0.0.1:8000/bookorder/'"
        #
        # cleaner_mail = ('You Booked', cleaner_msg, EMAIL_HOST_USER, [o.cleaner.user.email])
        # customer_mail = ('You Book', customer_msg, EMAIL_HOST_USER, [o.user.email])
        #
        # res = send_mass_mail((cleaner_mail, customer_mail), fail_silently=False)
        #
        # print(res)        # return render(request,'booking/postbooking.html')
        # d = BookingModel.objects.filter(user=request.user)
        return redirect('booking:bookinglist',pk=o.id)

@method_decorator(login_required, name='dispatch')
class Dutydetail(generic.ListView):
    template_name = 'booking/bookinglist.html'

    def get_queryset(self):
        return BookingModel.objects.filter(cleaner__user=self.request.user).order_by('-date')

@method_decorator(login_required, name='dispatch')
class BookingList(generic.ListView):
    template_name = 'booking/bookinglist.html'

    def get_queryset(self):
        return BookingModel.objects.filter(user=self.request.user).order_by('-date')
