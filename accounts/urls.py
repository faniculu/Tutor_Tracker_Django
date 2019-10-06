from django.urls import path
from .views import SignUpView, UserUpdateView , UserDetailView

urlpatterns = [
	path('signup/',SignUpView.as_view() , name = 'signup'),
	path('<int:pk>/update/',UserUpdateView.as_view(), name = 'update_user'),
	path('<int:pk>/',UserDetailView.as_view(), name = 'user_details')
]