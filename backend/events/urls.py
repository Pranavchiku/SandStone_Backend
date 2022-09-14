from django.contrib import admin
from django.urls import path, include
from .views import getSpeaker
urlpatterns = [
    path('get/speakers', getSpeaker, name='getSpeaker'),
]
