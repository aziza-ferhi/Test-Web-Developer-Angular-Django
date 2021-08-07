from django.conf.urls import url 
from django.urls import include, path
from employees import views 
from rest_framework import routers
from employees.views import employee_list


urlpatterns = [ 
    url(r'^api/employees$', views.employee_list),
    url(r'^api/employees/(?P<pk>[0-9]+)$', views.employee_detail),
]