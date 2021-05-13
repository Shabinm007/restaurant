from django.urls import path

from restaurantapp import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index', views.index, name='main'),
    path('about', views.about, name='about'),
    path('gallery_standard', views.gallery_standard, name='gallery_standard'),
    path('gallery_details', views.gallery_details, name='gallery_details'),
    path('rooms', views.rooms, name='rooms'),
    path('rooms_details', views.rooms_details, name='rooms_details'),
    path('service', views.service, name='service'),
    path('service_details', views.service_details, name='service_details'),
    path('staff', views.staff, name='staff'),
    path('staff_details', views.staff_details, name='staff_details'),
    path('contact', views.contact, name='contact'),
    path('booking_details', views.booking_details, name='booking_details'),
    path('rooms_status', views.rooms_status, name='rooms_status')

]

