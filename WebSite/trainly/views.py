from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse

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


def register(request):
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
            try:
                user.save()
            except IntegrityError:
                return HttpResponse("Email has been used.")
            return render(request, 'trainly/index.html')
    else:
        uf = UserForm()
        return render(request, 'trainly/register.html', {'uf': uf})


def index(request):
    return render(request, 'trainly/index.html')
