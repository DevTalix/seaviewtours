# tours/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('tours/', views.tours, name='tours'),
    path('tours/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('travel-tips/', views.travel_tips, name='traveltips'),
]