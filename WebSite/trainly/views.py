import hashlib

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import User, Admin, Faculty

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


class AddFacultyForm(forms.Form):
    email = forms.EmailField(label='Email')


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

            after_salt = uf.cleaned_data['pw'] + user.email
            after_salt.encode('utf-8')
            md5 = hashlib.md5()
            md5.update(after_salt)
            user.pw = md5.hexdigest()

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
            after_salt = uf.cleaned_data['pw'] + user_email
            m = hashlib.md5()
            m.update(after_salt.encode('utf-8'))
            user = User.objects.filter(email__exact=user_email, pw__exact=m.hexdigest())
            if user:
                user = user[0]
                response = HttpResponseRedirect('/trainly/')
                response.set_cookie('firstName', user.firstName, 3600)
                response.set_cookie('user_id', user.userID, 3600)
                return response
            else:
                return HttpResponse("User not exists or Password is wrong")
    else:
        uf = LoginForm()
        return render(request, 'trainly/login.html', {'uf': uf})


def logout(request):
    name = request.COOKIES.get('firstName', '')
    response = HttpResponse('You have already logout')
    if name:
        response.delete_cookie('firstName')
        response.delete_cookie('userID')
        return response
    else:
        return HttpResponse("Please login first")


def user_main_page(request):
    id = request.COOKIES.get('user_id', None)
    if id:
        id = int(id)
        user = User.objects.get(pk=id)

        context = {
            'first_name': user.firstName,
            'last_name': user.lastName,
            'email': user.email,
            'icon': user.profilePict,
            'country': user.country,
            'city': user.city,
            'street': user.street,
            'postal_code': user.postalCode
        }
        # if user is an admin
        try:
            admin = Admin.objects.get(pk=id)
        except ObjectDoesNotExist:
            context['admin'] = False
        else:
            context['admin'] = True

        # if user is a teacher
        try:
            faculty = Faculty.objects.get(pk=id)
        except ObjectDoesNotExist:
            context['faculty'] = False
        else:
            context['faculty'] = True
            context['affiliation'] = faculty.affiliation
            context['website'] = faculty.website
            context['title'] = faculty.title

        return render(request, 'trainly/user_main_page.html', context)
    else:
        return HttpResponse("Please login first")
