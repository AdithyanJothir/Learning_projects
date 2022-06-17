from django import views
from django.contrib import admin
from django.urls import path
from .views import Employeeview

urlpatterns = [
    path('employee/', Employeeview.as_view() ,name  = "employee_list"),
    
]
