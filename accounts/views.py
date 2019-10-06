from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationForm, CustomChangeForm
from .models import MyCustomUser
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

# Create your views here.
class SignUpView(CreateView):
	form_class = CustomCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

class UserUpdateView(UpdateView):
	model = MyCustomUser
	fields = ['username','email','first_name', 'last_name', 'stdno']
	template_name = 'user_update_form.html'

class UserDetailView(DetailView):
	model = MyCustomUser
	template_name = 'user_details.html'