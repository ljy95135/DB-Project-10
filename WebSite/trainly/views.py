from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import User

from django import forms


class UserForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=50)
    lastName = forms.CharField(label='Last Name', max_length=50)
    country = forms.CharField(label='Country', max_length=50)
    city = forms.CharField(label='City', max_length=50)
    street = forms.CharField(label='Street', max_length=200)
    postalCode = forms.CharField(label='Postal Code', max_length=20)
    pw = forms.CharField(label='Password', widget=forms.PasswordInput())
    email = forms.EmailField(label='Email')


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    pw = forms.CharField(label='Password', widget=forms.PasswordInput())


# TODO add check input
def register(request):
    name = request.COOKIES.get("firstName", '')
    if not name == '':
        return HttpResponse("You have already log in")
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            user = User()
            user.email = uf.cleaned_data['email']
            user.firstName = uf.cleaned_data['firstName']
            user.lastName = uf.cleaned_data['lastName']
            user.pw = uf.cleaned_data['pw']
            user.profilePict = "default.jpg"
            user.country = uf.cleaned_data['country']
            user.city = uf.cleaned_data['city']
            user.street = uf.cleaned_data['street']
            user.postalCode = uf.cleaned_data['postalCode']
            try:  # Error when it has been registered
                user.save()
            except IntegrityError:
                return HttpResponse("Email has been used.")
            return render(request, 'trainly/index.html')
    else:
        uf = UserForm()
        return render(request, 'trainly/register.html', {'uf': uf})


def index(request):
    name = request.COOKIES.get("firstName", '')
    return render(request, 'trainly/index.html', {'name': name})


def login(request):
    name = request.COOKIES.get("firstName", '')
    if not name == '':
        return HttpResponse("You have already log in")
    if request.method == "POST":
        uf = LoginForm(request.POST)
        if uf.is_valid():
            user_email = uf.cleaned_data['email']
            user_pw = uf.cleaned_data['pw']
            user = User.objects.filter(email__exact=user_email, pw__exact=user_pw)
            if user:
                user = user[0]
                # TODO go to main page
                response = HttpResponseRedirect('/trainly/')
                response.set_cookie('firstName', user.firstName, 3600)
                return response
            else:
                return HttpResponse("User not exist")
    else:
        uf = LoginForm()
        return render(request, 'trainly/login.html', {'uf': uf})


def logout(request):
    name = request.COOKIES.get('firstName', '')
    response = HttpResponse('You have already logout')
    if name:
        response.delete_cookie('firstName')
        return response
    else:
        return HttpResponse("Please login first")

# TODO main page of the user
def user_main_page(request):
    pass
