from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone =models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    body = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


    # def clean(self):
    #     data = self.cleaned_data
    #     email = self.cleaned_data.get('email')
    #     email2 Contact.objects.get('email')
    #     if email in email2:
    #         return 
