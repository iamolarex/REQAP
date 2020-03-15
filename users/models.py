from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    school = (
        ('sict','SICT'),
        ('set','SET')
    )
    faculty = models.CharField(max_length=12, choices=school)
    department = models.CharField(max_length=65)

    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gradution_date = models.DateField()
    has_graduated = models.BooleanField(default=False)

class Staff(models.Model):
    """
    For now this takes care of only Academic staffs
    """
    staff_offices = (
        ('normal', 'Normal'),
        ('LA', 'Level Adviser'),
        ('EO', 'Exam officer'),
        ('HOD', 'Head of Department'),
        ('DOS', 'Dean of School')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    office = models.CharField(max_length=25, choices=staff_offices)