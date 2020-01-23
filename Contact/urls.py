from django.conf import settings
from django.contrib import admin
from django.urls import path

from .views import Contact_page


urlpatterns = [
    path('', Contact_page, name='contact'),
    
]