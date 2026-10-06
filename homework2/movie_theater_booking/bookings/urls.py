from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"movies", views.MovieViewSet, basename="movies")
router.register(r"seats", views.SeatViewSet, basename="seats")
router.register(r"bookings", views.BookingViewSet, basename="bookings")

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include(router.urls)),
    path("booking_history", views.booking_history, name="booking_history"),
    path("movies/<int:movie_id>/book/", views.book_seat, name="book_seat")
]