import hashlib
import datetime
import random

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import User, Admin, Faculty, Course, BuyCourse, Interested, Secondarytopic, Coursematerial, \
    CompleteMaterial

from django import forms

month_list = [None, 'Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']


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
    website = forms.CharField(label='Website', max_length=200)
    affiliation = forms.CharField(label='Affiliation', max_length=50)
    title = forms.CharField(label='Title', max_length=300)


class AddAdminForm(forms.Form):
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
    user_id = request.COOKIES.get('user_id', None)
    if user_id:
        user_id = int(user_id)
        user = User.objects.get(pk=user_id)

        context = {
            'uid': user_id,
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
            Admin.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            context['admin'] = False
        else:
            context['admin'] = True

        # if user is a teacher
        try:
            faculty = Faculty.objects.get(pk=user_id)
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


def add_faculty(request):
    admin_id = request.COOKIES.get('user_id', None)
    if admin_id is None:
        return HttpResponse("Please login first")

    try:
        admin = Admin.objects.get(pk=admin_id)
    except Admin.DoesNotExist:
        return HttpResponse("Only admin can access this page.")

    if request.method == "POST":
        uf = AddFacultyForm(request.POST)
        if uf.is_valid():
            user_email = uf.cleaned_data['email']
            try:
                user = User.objects.get(email=user_email)
            except User.DoesNotExist:
                return HttpResponse("User not exist")

            try:
                Faculty.objects.get(userID=user.userID)
            except Faculty.DoesNotExist:
                faculty = Faculty()
                faculty.userID = user
                faculty.website = uf.cleaned_data['website']
                faculty.affiliation = uf.cleaned_data['affiliation']
                faculty.title = uf.cleaned_data['title']
                faculty.grantAdmin = admin
                faculty.grantTime = datetime.datetime.now()
                faculty.save()
                return HttpResponse("Done!")
            else:
                return HttpResponse("This user has been a faculty")
    else:
        uf = AddFacultyForm()
        return render(request, 'trainly/add_faculty.html', {'uf': uf})


def add_admin(request):
    admin_id = request.COOKIES.get('user_id', None)
    if admin_id is None:
        return HttpResponse("Please login first")

    try:
        admin = Admin.objects.get(pk=admin_id)
    except Admin.DoesNotExist:
        return HttpResponse("Only admin can access this page.")

    if request.method == "POST":
        uf = AddAdminForm(request.POST)
        if uf.is_valid():
            new_user = uf.cleaned_data['email']
            try:
                new_admin_user = User.objects.get(email=new_user)
            except User.DoesNotExist:
                return HttpResponse("User not exist")

            try:
                Admin.objects.get(userID=new_admin_user.userID)
            except Admin.DoesNotExist:
                new_admin = Admin()
                new_admin.userID = new_admin_user
                new_admin.grantAdmin = admin
                new_admin.grantTime = datetime.datetime.now()
                new_admin.save()
                return HttpResponse("Done!")
            else:
                return HttpResponse("This user has been a Admin")
    else:
        uf = AddAdminForm()
        return render(request, 'trainly/add_admin.html', {'uf': uf})


def add_course(request, cid):
    user_id = request.COOKIES.get('user_id', None)
    if user_id is None:
        return HttpResponse("Please login first")

    user = User.objects.get(pk=user_id)

    try:
        course = Course.objects.get(pk=cid)
    except Course.DoesNotExist:
        return HttpResponse("No such Course")

    try:
        BuyCourse.objects.get(userID=user, cid=course)
    except BuyCourse.DoesNotExist:
        buy = BuyCourse()
        buy.userID = user
        buy.cid = course
        buy.buyTime = datetime.datetime.now()
        # code is year+month+date+time+random number
        code = buy.buyTime.strftime('%Y%m%d%H%m')
        code += str(random.randint(100000, 999999))
        buy.code = code
        buy.isComplete = 0
        buy.rating = -1
        buy.save(force_insert=True)
        return HttpResponse("Done!")
    else:
        return HttpResponse("You have already bought it!")


def enrolled_courses(request, uid):
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return HttpResponse('No such User')

    courses = [bc.cid for bc in BuyCourse.objects.filter(userID=user)]
    # no rates available now
    # courses = sorted(courses, key=lambda x: x.avgRate)
    context = {'courses': courses}
    return render(request, 'trainly/enrolled_courses.html', context)


def completed_courses(request, uid):
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return HttpResponse('No such User')
    courses = [bc.cid for bc in BuyCourse.objects.filter(userID=user, isComplete=1)]
    # no rates available now
    # courses = sorted(courses, key=lambda x: x.avgRate)
    context = {'courses': courses}

    return render(request, 'trainly/completed_courses.html', context)


def interested_courses(request, uid):
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return HttpResponse('No such User')
    courses = [bc.cid for bc in Interested.objects.filter(userID=user)]
    context = {'courses': courses}
    return render(request, 'trainly/interested_courses.html', context)


class CoursesView(generic.ListView):
    template_name = 'trainly/courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()


def course_page(request, cid):
    # basic info section
    try:
        course = Course.objects.get(pk=cid)
    except Course.DoesNotExist:
        return HttpResponse("No such Course")

    context = {"course": course}
    topics = [t.tid.name for t in Secondarytopic.objects.filter(cid=course)]
    context['topics'] = topics

    user_id = request.COOKIES.get('user_id', None)

    # If this is a user enrolled in the course
    if user_id is None:
        context['enrolled'] = False
        return render(request, 'trainly/course.html', context)

    user = User.objects.get(pk=user_id)
    try:
        BuyCourse.objects.get(userID=user, cid=course)
    except BuyCourse.DoesNotExist:
        context['enrolled'] = False
        return render(request, 'trainly/course.html', context)
    context['enrolled'] = True
    course_materials = [cm for cm in Coursematerial.objects.filter(cid=course)]
    context['course_materials'] = course_materials

    return render(request, 'trainly/course.html', context)


def learn_material(request, cmid):
    user_id = request.COOKIES.get('user_id', None)
    if user_id is None:
        return HttpResponse("Please login first")
    user = User.objects.get(pk=user_id)

    try:
        course_material = Coursematerial.objects.get(pk=cmid)
    except Coursematerial.DoesNotExist:
        return HttpResponse("No such Material")

    try:
        bc = BuyCourse.objects.get(userID=user, cid=course_material.cid)
    except BuyCourse.DoesNotExist:
        return HttpResponse("You must buy this course first!")

    # Complete material
    try:
        CompleteMaterial.objects.get(userID=user, cmid=course_material)
    except CompleteMaterial.DoesNotExist:
        pass
    else:
        return HttpResponse("You learn it again, good!")
    cm = CompleteMaterial()
    cm.userID = user
    cm.cmid = course_material
    cm.completeTime = datetime.datetime.now()
    cm.save()

    # Maybe it will finish the course
    try:
        for material in Coursematerial.objects.filter(cid=course_material.cid):
            CompleteMaterial.objects.get(userID=user, cmid=material)
    except CompleteMaterial.DoesNotExist:
        return HttpResponse("You learn the material, you can still learn this course!")
    else:
        bc.isComplete = 1
        bc.completeTime = datetime.datetime.now()
        bc.save(update_fields=('isComplete', 'completeTime'))
        return HttpResponse("You learn the material, you also finish the course!")


def certification(request, cid):
    user_id = request.COOKIES.get('user_id', None)
    if user_id is None:
        return HttpResponse("Please login first")
    user = User.objects.get(pk=user_id)

    try:
        course = Course.objects.get(pk=cid)
    except Course.DoesNotExist:
        return HttpResponse("No such Course")

    try:
        bc = BuyCourse.objects.get(userID=user, cid=course)
    except BuyCourse.DoesNotExist:
        return HttpResponse("You are not enrolled in this course.")

    if bc.isComplete != 1:
        return HttpResponse("Please finish it first.")

    month = bc.completeTime.date().strftime('%m')
    month_name = month_list[int(month)]
    day_year_name = bc.completeTime.date().strftime(', %d, %Y')

    context = {'user': user, 'time': month_name + day_year_name, 'course': bc.cid.name}
    return render(request, 'trainly/certification.html', context)
