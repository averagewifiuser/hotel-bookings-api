from django.db import models
from django.utils import timezone

def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)

class Room(models.Model):
    number = models.CharField(max_length=30, blank=False, unique=True)
    room_type = models.CharField(max_length=30, choices=[('standard', 'standard'),
    ('deluxe', 'deluxe'), ('double', 'double')])
    price = models.FloatField(blank=False)
    is_booked = models.BooleanField(default=False)



class Booking(models.Model):
    '''
    room_id fk default null
    booked_by fk default null
    starts default timezone.now
    ends timezone.now + 1 day
    confirmed default false

    '''
    room = models.ForeignKey(Room, default=None)
    #booked_by = models.ForeignKey('customers.Customer', default=None)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=one_day_hence)
    confirmed = models.BooleanField(default=False)
    