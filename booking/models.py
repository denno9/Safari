from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=120)
    midlename = models.CharField(blank=True,max_length=120)
    lastname = models.CharField(max_length=120)
    checkin = models.DateField
    checkout = models.DateField
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=230)

