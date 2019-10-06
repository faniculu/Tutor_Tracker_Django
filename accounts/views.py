from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUpView(generic.CreateView):
	form_class = CustomCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'