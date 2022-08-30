from django.shortcuts import render
from rest_framework import generics,filters
from .models import Student,Department
from .serializer import StudentSerializer,DepartmentSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.



class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    filter_backends =[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]

    filterset_fields=["name","department","level","status"]
    search_fields = ["name","department","level","status"]
    ordering_fields = ["name","department","level","status"]



class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer