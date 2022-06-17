from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class Employeeview(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)






