from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.home_view, name='home'),
    path('v1/calendar/init/', views.GoogleCalendarInitView, name='google_permission'),
    path('v1/calendar/redirect/', views.GoogleCalendarRedirectView, name='google_redirect')
]
