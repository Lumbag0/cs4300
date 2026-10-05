from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    duration = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.title}"

class Seat(models.Model):
    seat_number = models.CharField(max_length=3)
    booking_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat:{self.seat_number}"

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Set so one seat can be booked only once
        constraints = [models.UniqueConstraint(fields=["movie", "seat"], name="unique_booking_per_movie_seat")]

    def __str__(self):
        return f"{self.user.username}: {self.seat}"
    