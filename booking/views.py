from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
# from .forms import ContactForm
from django.core.mail import EmailMessage,send_mail


# Create your views here.
def bookingView(request):
    return render(request,"booking_page.html",{})
