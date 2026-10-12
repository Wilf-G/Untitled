from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('contact/', views.contact, name = 'contact'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('events/', views.event_list, name = 'events')
]