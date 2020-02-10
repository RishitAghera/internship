from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from .forms import RegistrationForm, LoginForm, CleanerRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import messages
from django.views import generic
from .models import User, City


class RegistrationView(View):
    def get(self, request):
        rform = RegistrationForm()
        return render(request, 'registration/registration.html', {'form': rform})

    def post(self, request):
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            rform.save()
        return redirect('registration:login')


class LoginView(View):
    def get(self, request):
        lform = LoginForm()
        return render(request, 'registration/login.html', {'form': lform})

    def post(self, request):
        form1 = LoginForm(data=request.POST)
        if form1.is_valid():
            print('isvalid')
            contact = form1.cleaned_data.get('contact')
            password = form1.cleaned_data.get('password')
            user = authenticate(contact=contact, password=password)
            if user is not None:
                login(request, user)
                return redirect('registration:index')
                print("logged in")
            else:
                messages.error(request, 'User Not Found please Enter Valid data' + str(form1.errors))
        return render(request, 'registration/login.html', {'form': form1})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("registration:index")

def index(request):
    return render(request,'registration/index.html')


class CleanerRegistrationView(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        form = CleanerRegistrationForm()
        return render(request, 'registration/cleaner_registration_form.html', {'form': form})

    @method_decorator(login_required, name='dispatch')
    def post(self,request):
        form=CleanerRegistrationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            request.user.is_cleaner=True
            request.user.save()
            obj.save()
            return redirect("registration:profile",pk=request.user.pk)

class ProfileView(generic.DetailView):
    model=User
    template_name = 'registration/profile.html'
    extra_context = {'form':CleanerRegistrationForm()}

class Booking(View):

    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/registration.html', {'form': form})

    @method_decorator(login_required, name='dispatch')
    def post(self, request):
        rform = RegistrationForm(request.POST)
        if rform.is_valid():

            rform.save()
        return render(request, 'registration/index.html', {'form': rform})


class CityView(generic.ListView):
    template_name = 'registration/city.html'

    def get_queryset(self):
        return City.objects.all()

def validate_contact(request):
    contact = request.GET.get('contact',None)
    data = {
        'is_taken': User.objects.filter(contact_iexact=contact).exists()
    }
    return JsonResponse(data)