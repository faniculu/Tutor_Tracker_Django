from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentSignUpForm, LectureSignUpForm, CustomChangeForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

# Create your views here.
def SignUp(request):
	return render(request , 'signup.html')

class StudentSignUpView(CreateView):
	form_class = StudentSignUpForm
	success_url = reverse_lazy('login')
	template_name = 'specific_signup.html'

class LectureSignUpView(CreateView):
	form_class = LectureSignUpForm
	success_url = reverse_lazy('login')
	template_name = 'specific_signup.html'

class UserUpdateView(LoginRequiredMixin,UpdateView):
	model = CustomUser
	fields = ['username','email','first_name', 'last_name']
	template_name = 'user_update_form.html'

class UserDetailView(LoginRequiredMixin,DetailView):
	model = CustomUser
	template_name = 'user_details.html'