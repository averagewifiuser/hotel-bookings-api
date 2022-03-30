from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    #TODO: update to use phonenumbers
    phone_number = models.CharField(max_length=13, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    

class Payment(models.Model):
    paid_by = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    paid_on = models.DateTimeField(default=timezone.now)
    paid_for = models.ForeignKey('bookings.Booking', on_delete=models.RESTRICT)