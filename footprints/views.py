from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User

from django.core.mail import EmailMessage,send_mail
import datetime
from django.conf import settings


def Home_page(request):
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    
    context= {
        "year":year
        
    }
    return render(request,"home_page.html",context)

def About_page(request):
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    
    context= {
        "year":year
        
    }
    return render(request,"about_page.html",context)


def Booking_page(request):
    return render(request,"booking_page.html",{})