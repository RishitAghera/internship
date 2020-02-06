from django.contrib import admin
from django.urls import path,include
from .views import *



app_name='booking'

urlpatterns = [
    #booking/book/
    path('book/',BookingView.as_view(),name='book'),
    path('bookingdetail/<int:pk>/',BookingList.as_view(),name='bookinglist'),
    path('bookingsave/',BookingSave.as_view(),name='bookingsave'),
    # path('postbooking/',PostBooking.as_view(),name='postbooking')

]