from django.conf.urls import url

from . import views

app_name = 'trainly'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
]
