from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import bookingView

urlpatterns = [

    path('contact/', bookingView,name='booking'),

]