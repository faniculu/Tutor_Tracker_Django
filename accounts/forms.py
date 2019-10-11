from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import CustomUser , Student
from .choices import ACADEMIC_YEAR

#student
class StudentSignUpForm(UserCreationForm):
	student_number = forms.IntegerField(required = True, min_value = 100000)
	academic_year = forms.ChoiceField(required = True, choices = ACADEMIC_YEAR, widget = forms.Select )

	class Meta:
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('email',) 

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_student = True
		user.save()
		student = Student.objects.create(user=user, 
			student_number = self.cleaned_data.get('student_number'), 
			academic_year = self.cleaned_data.get('academic_year'))
		return user
		


#lecture
class LectureSignUpForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('email',) 

	def save(self, commit = True):
		user = super().save(commit = False)
		user.is_lecture = True
		if commit:
			user.save()
		return user
	


class CustomChangeForm(UserChangeForm):

	class Meta:

		model = CustomUser
		fields = UserChangeForm.Meta.fields



