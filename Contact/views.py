from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage,send_mail
import datetime
from django.conf import settings

# Create your views here.
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
            sender = settings.EMAIL_HOST_USER
            subject = form.cleaned_data.get("subject")
            body = form.cleaned_data.get("body")
            recepient = ['denno.tz@gmail.com']
            send_mail(subject, body, sender, recepient)
            context['form'] = ContactForm()
            print(sender_email)
            print(body)
            print(subject)
            form.save()

            return redirect('/')
        

    
    return render(request,"contact_page.html",context)