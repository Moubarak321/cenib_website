from django.urls import path
from . import views



urlpatterns=[
    path('about', views.about, name='about'),
    path('trainers', views.trainers, name='trainers'),
    path('courses', views.courses, name='courses'),
    path('pricing', views.pricing, name='pricing'),
    path('events', views.events, name='events'),
    path('contact', views.contact, name='contact'),
    path('course_details/<int:id>', views.course_details, name='course_details')
]