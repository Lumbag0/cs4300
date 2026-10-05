from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from .models import Movie, Seat, Booking

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, "bookings/movie_list.html", {"movies":movies})

@login_required
def booking_history(request):
    return render(request, "bookings/booking_history.html")

@login_required
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    seats = Seat.objects.order_by("seat_number")
    return render(request, "bookings/seat_booking.html", {"movie": movie, "seats": seats})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer