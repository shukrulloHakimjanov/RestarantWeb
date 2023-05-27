from django.urls import path
from . import views

urlpatterns = [
     path('', views.home_page, name='home_page'),
     path('about/', views.about, name='about'),
     path('service/', views.service, name='service'),
     path('booking/', views.booking, name='booking'),
     path('menu/', views.menu, name='menu'),
     path('contact/', views.contact, name='contact'),
]