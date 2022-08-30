
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('api',views.StudentList.as_view(), name='api'),
    path('myapi/<int:pk>',views.StudentDetail.as_view(), name='singleapi'),
]
