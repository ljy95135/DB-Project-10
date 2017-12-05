from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'trainly'
urlpatterns = \
    [
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.login, name='login'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^main/$', views.user_main_page, name='main'),
    ]
