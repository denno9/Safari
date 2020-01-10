from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    firstname = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput( attrs={"class":"form-control"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    

