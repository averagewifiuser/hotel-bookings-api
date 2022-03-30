from django.db import models
from django.utils import timezone, crypto
import string

def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)

def generate_room_code():
    return crypto.get_random_string(9, allowed_chars=string.ascii_uppercase + string.digits)


class Room(models.Model):
    number = models.CharField(max_length=30, blank=False, unique=True)
    room_type = models.CharField(max_length=30, choices=[('standard', 'standard'),
    ('deluxe', 'deluxe'), ('double', 'double')])
    price = models.FloatField(blank=False)
    is_booked = models.BooleanField(default=False)


class Booking(models.Model):
    room = models.ForeignKey(Room, default=None, on_delete=models.RESTRICT)
    booked_by = models.ForeignKey('customers.Customer', default=None, on_delete=models.RESTRICT)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=one_day_hence)
    code = models.CharField(default=generate_room_code, max_length=10, unique=True)
    confirmed = models.BooleanField(default=False)
