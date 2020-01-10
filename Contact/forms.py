from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm,TextInput,Textarea,EmailInput,NumberInput

from .models import Contact
class ContactForm(forms.ModelForm):
    """Form definition 
    
    ."""

    class Meta:
        """Meta definition f
        
        form."""

        model=Contact

        fields = ('__all__')
        
    
        widgets = {
            'email' : EmailInput(attrs={"class":"form-control"}),
            'firstname': TextInput(attrs={"class":"form-control"}),
            'lastname': TextInput(attrs={"class":"form-control"}),
            'phone' : NumberInput(attrs={"class":"form-control"}),
            'subject' :  TextInput(attrs={"class":"form-control"}),
            'body'  : Textarea(attrs={"class":"form-control"})
        }
