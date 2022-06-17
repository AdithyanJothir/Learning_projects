from django import views
from django.contrib import admin
from django.urls import path
from .views import Employeeview,EmployeeDetailview

urlpatterns = [
    path('employee/', Employeeview.as_view() ,name  = "employee_list"),
    path('emp_detail/<int:id>',EmployeeDetailview.as_view(),name = "employee_detailview"),
    
]
