from django.conf.urls import url
from django.urls import path

from . import views
from .views import *
app_name='registration'

urlpatterns = [
    path('',views.index,name='index'),
    path('registration/',RegistrationView.as_view(),name='registration'),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('cleaner-registration/',CleanerRegistrationView.as_view(),name='cleaner-registration'),
    path('profile/<int:pk>/',ProfileView.as_view(),name="profile"),
    path('booking/',Booking.as_view(),name="booking"),
    path('city/',CityView.as_view(),name='city'),
    url(r'^ajax/validate_contact/$', views.validate_contact, name='validate_contact'),
]