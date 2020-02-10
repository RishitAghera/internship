from django.contrib import admin
from django.urls import path,include
from .views import *



app_name='booking'

urlpatterns = [
    #booking/book/
    path('book/',BookingView.as_view(),name='book'),
    path('bookingdetail/<int:pk>/',BookingDetail.as_view(),name='bookinglist'),
    path('dutydetail/<int:pk>/',Dutydetail.as_view(),name='dutydetail'),
    path('bookingsave/',BookingSave.as_view(),name='bookingsave'),
    path('mybookinglist/',BookingList.as_view(),name='mybookinglist'),
    path('delete/<int:pk>/',DeleteBooking.as_view(),name='deletebooking')
    # path('postbooking/',PostBooking.as_view(),name='postbooking')

]