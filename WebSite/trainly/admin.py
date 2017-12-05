from django.contrib import admin

from .models import User, Admin, Faculty

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Faculty)
