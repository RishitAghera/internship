from django import forms

from booking.models import BookingModel
from .models import User, City,Cleaner
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.core.validators import RegexValidator

phonenumberrexp=RegexValidator(regex='^[0-9]{10}$',message="Enter Valid Mobile Number")


class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=('contact','first_name','last_name','email','password1','password2')

class LoginForm(forms.Form):

    contact=forms.CharField(max_length=12, label="Enter Contact")
    password=forms.CharField(max_length=20,label="Enter Password",widget=forms.PasswordInput())

class CleanerRegistrationForm(forms.ModelForm):
    city=forms.ModelChoiceField(label='select city',queryset=City.objects.all())
    class Meta:
        model=Cleaner
        fields=('city',)


