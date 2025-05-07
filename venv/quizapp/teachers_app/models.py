from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from students_app.models import Department, Semester
from django.utils import timezone
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')
    teacher_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='teachers')
    courses = models.ManyToManyField(Course, related_name='teachers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_quizzes_created = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"