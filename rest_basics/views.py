from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from requests import delete
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmployeeSerializer
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


    
class EmployeeDetailview(APIView):
    
    def get_object(self,id):
        try:
           return Employee.objects.get(id=id)
            

        except Employee.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
        
    def get(self,request,id):
        employee = self.get_object(id)
        serialized = EmployeeSerializer(employee)
        return Response(serialized.data)
    
    def put(self,request,id):
        employee = self.get_object(id)
        serialized = EmployeeSerializer(employee , data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        employee = self.get_object(id)
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

        
        




