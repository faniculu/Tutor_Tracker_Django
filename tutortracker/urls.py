from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    path('tutortracker/', HomePageView.as_view(), name='home'),
    path('tutortracker/about/', AboutPageView.as_view(), name = 'about'),
]
