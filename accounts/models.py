from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from .choices import ACADEMIC_YEAR
# Create your models here

class CustomUser(AbstractUser):	
	is_student = models.BooleanField(default = False)
	is_lecture = models.BooleanField(default = False)
	

	def get_absolute_url(self):
		return reverse('user_details', args = [str(self.id)])

	def __str__(self):
		return self.username

class Student(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
	student_number = models.PositiveIntegerField(unique = True)
	academic_year = models.CharField(max_length = 10,choices = ACADEMIC_YEAR)

	def __str__(self):
		return self.user