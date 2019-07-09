# Add url paths for workflow app
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import django.contrib.auth.views
from django.urls import path
from . import views
from rest_framework.authtoken import views as authviews

admin.autodiscover()

urlpatterns = [
    path('employees/', views.ListEmployees.as_view(), name="employees"),
    path('employees/<int:emp_ID>/', views.SingleEmployee.as_view()),
    path('pictures/', views.ListPictures.as_view(), name="allpictures"),
    path('pictures/<int:emp_ID>/', views.EmployeePictures.as_view()),
    path('pictures/<str:name>/', views.SinglePicture.as_view()),
    path('temp-photos/', views.ListTempPhotos.as_view(), name="alltempphotos"),
    path('token-auth/', authviews.obtain_auth_token),
]
