from django.db import models

# Create your models here.

STATUS =(
('A','Active'),
('N','Not Active'),

)

class Department(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    faculty = models.CharField(max_length=20, null=True)



    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=50, null=True)
    age= models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.IntegerField(default=100)
    email = models.EmailField(max_length=40)
    phoneNumber = models.IntegerField()
    status= models.CharField(max_length=20, choices=STATUS, default='A')
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-date_created',)


    
    def __str__(self):
        return self.name




