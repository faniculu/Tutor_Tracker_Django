from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import StudentSignUpForm, LectureSignUpForm, CustomChangeForm
from .models import CustomUser , Student



admin.site.register(CustomUser,UserAdmin)
admin.site.register(Student)