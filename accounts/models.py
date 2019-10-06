from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here

class MyCustomUser(AbstractUser):

	stdno = models.PositiveIntegerField(null = True, blank = True, unique = True)

	def get_absolute_url(self):
		return reverse('user_details', args = [str(self.id)])