from django.urls import path
from .views import (SignUp, UserUpdateView , UserDetailView ,StudentSignUpView , LectureSignUpView)
from . import views
urlpatterns = [
	path('signup/', views.SignUp , name = 'signup'),
	path('signup/student/',StudentSignUpView.as_view(), name = 'student_signup'),
	path('signup/lecture/',LectureSignUpView.as_view(), name = 'lecture_signup'),
	path('<int:pk>/update/',UserUpdateView.as_view(), name = 'update_user'),
	path('<int:pk>/',UserDetailView.as_view(), name = 'user_details')
]