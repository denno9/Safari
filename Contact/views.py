from django.shortcuts import render

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
            firsname = form.cleaned_data.get("firstname")
            lastname = form.cleaned_data.get("lastname")
            sender_email  = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            body = form.cleaned_data.get("body")
            recepient = ['denno.tz@gmail.com']
            # send_mail(subject,body,sender_email,recepient)
            context['form'] = ContactForm()
            form.save()

        print(request.POST)
        # form = ContactForm(request.POST or None)

    context['form'] = ContactForm()
    return render(request,"contact_page.html",context)