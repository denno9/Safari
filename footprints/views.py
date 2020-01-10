from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
# from .forms import ContactForm
from Contact.forms import ContactForm
from django.core.mail import EmailMessage,send_mail
import datetime


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

def Contact_page(request):
    form = ContactForm(request.POST or None)
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    context= {
        "form":form,
         "year": year
    }
   
    if request.method =="POST":
        if form.is_valid():
            firstname = form.cleaned_data.get("firstname")
            lastname = form.cleaned_data.get("lastname")
            sender_email  = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            body = form.cleaned_data.get("body")
            recepient = ['denno.tz@gmail.com']
            # send_mail(subject,body,sender_email,recepient)
            context['form'] = ContactForm()
            print(sender_email)
            form.save()

            return redirect('/')
        

    
    return render(request,"contact_page.html",context)


def Booking_page(request):
    return render(request,"booking_page.html",{})