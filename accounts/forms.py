from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import MyCustomUser

class CustomCreationForm(UserCreationForm):

	class Meta:

		model = MyCustomUser
		fields = UserCreationForm.Meta.fields + ('stdno',) #adding the new field to the form



class CustomChangeForm(UserChangeForm):

	class Meta:

		model = MyCustomUser
		fields = UserChangeForm.Meta.fields



