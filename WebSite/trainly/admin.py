from django.contrib import admin

from .models import User, Admin, Faculty, Course, BuyCourse

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(BuyCourse)
