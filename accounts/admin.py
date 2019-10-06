from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomCreationForm, CustomChangeForm
from .models import MyCustomUser


class CustomUserAdmin(UserAdmin):

	add_form = CustomCreationForm
	form = CustomChangeForm
	model = MyCustomUser
	list_display = ['email', 'username', 'stdno', 'is_staff', ] 


admin.site.register(MyCustomUser, CustomUserAdmin)