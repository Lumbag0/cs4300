from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
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

    if request.method == "GET":
        seats = Seat.objects.order_by("seat_number")
        return render(request, "bookings/seat_booking.html", {"movie": movie, "seats": seats})
    
    elif request.method == "POST":
        seat_id = get_object_or_404(Seat, pk=request.POST.get("seat"))

        # Present an error message if the user tries to select a seat that is already taken
        # Else book requested seat
        if seat_id.booking_status == True:
            messages.error(request, "This seat is already booked. Please try another")
        else:
            Booking.objects.create(movie=movie, seat=seat_id, user=request.user)
            seat_id.booking_status = True
            seat_id.save()
            messages.success(request, f"Seat {seat_id.seat_number} is booked for {movie.title}!")

        return redirect("book_seat", movie_id=movie.id)
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        seat = serializer.validated_data["seat"]
        if seat.booking_status == True:
            raise ValidationError("ERROR: This seat is already booked")
        else:
            serializer.save(user=self.request.user)
            seat.booking_status = True
            seat.save()