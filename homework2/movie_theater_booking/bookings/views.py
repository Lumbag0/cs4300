from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from .models import Movie, Seat, Booking

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, "bookings/movie_list.html", {"movies":movies})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer