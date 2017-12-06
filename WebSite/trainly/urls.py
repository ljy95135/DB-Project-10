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
        url(r'^add_faculty/$', views.add_faculty, name='add_faculty'),
        url(r'^add_admin/$', views.add_admin, name='add_admin'),
        url(r'^course_page/(?P<cid>[0-9]+)$', views.course_page, name='courses_page'),
        url(r'^courses/$', views.CoursesView.as_view(), name='courses'),
        url(r'^add_course/(?P<cid>[0-9]+)$', views.add_course, name='add_course'),
        url(r'^completed_courses/(?P<uid>[0-9]+)$', views.completed_courses, name='completed_courses'),
        url(r'^interested_courses/(?P<uid>[0-9]+)$', views.interested_courses, name='interested_courses'),
        url(r'^enrolled_courses/(?P<uid>[0-9]+)$', views.enrolled_courses, name='enrolled_courses'),
        url(r'^learn_material/(?P<cmid>[0-9]+)$', views.learn_material, name='learn_material'),
        
    ]
