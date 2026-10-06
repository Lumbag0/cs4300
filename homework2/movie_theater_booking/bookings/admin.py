from django.contrib import admin
from .models import Movie, Booking, Seat

# Register your models here.
admin.site.register(Movie)
admin.site.register(Booking)
admin.site.register(Seat)