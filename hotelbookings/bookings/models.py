from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=30, blank=False, unique=True)
    room_type = models.CharField(max_length=30, choices=[('standard', 'standard'),
    ('deluxe', 'deluxe'), ('double', 'double')])
    price = models.FloatField(blank=False)
    is_booked = models.BooleanField(default=False)



