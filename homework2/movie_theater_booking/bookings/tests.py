from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.urls import reverse
from rest_framework.test import APIClient
from datetime import date
from .models import Movie, Seat, Booking
# Create your tests here.

class BookingBase(TestCase):
    # Setup:
    #   1 Movie:
    #       2 Seats
    #   2 Users
    
    def setUp(self):
        # Define Movie
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Description for Test Movie",
            release_date = date(2026, 10, 5),
            duration=120,
        )

        # Define Seats
        self.seat_a1 = Seat.objects.create(seat_number = "A1")
        self.seat_a2 = Seat.objects.create(seat_number = "A2")

        # Define Users
        self.user1 = User.objects.create_user(username="Wirt", password="Str0nGP@s$coDE")
        self.user2 = User.objects.create_user(username="Greg", password="Jason-Funderburker")

        # Key endpoints
        self.booking_page = reverse("book_seat", args=[self.movie.id])
        self.history_page = reverse("booking_history")
        self.login_page = reverse("login")

class TestLogin(BookingBase):
    # Test that when logging in with a valid username but invalid password, the user does not login and 
    # stays on the login page.
    def test_login_with_wrong_password(self):
        response = self.client.post(
            self.login_page, 
            {
                "username": "Wirt", 
                "password": "a-wrong-password"
            }
        )
        # Confirm page stays on login page + confirm no one is logged in
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("_auth_user_id", self.client.session)

    # Test that when logging in with a valid username and password, that you redirect to the home page
    def test_login_with_correct_password(self):
        response = self.client.post(
            self.login_page,
            {
                "username": "Wirt",
                "password": "Str0nGP@s$coDE"
            }
        )
        # Confirm the page redirects to the home page and that a user session is created
        self.assertRedirects(response, "/")
        self.assertIn("_auth_user_id", self.client.session)
        
class AuthenticatedBookingTests(BookingBase):
    def setUp(self):
        super().setUp()
        self.client.login(username = "Wirt", password = "Str0nGP@s$coDE")

    def test_booking_unoccupied_seat_succeeds(self):
        self.client.post(self.booking_page, {"seat": self.seat_a1.id})
        self.assertTrue(
            Booking.objects.filter(
                movie = self.movie, seat = self.seat_a1, user = self.user1
            ).exists()
        )

    def test_booking_occupied_seat_fails(self):
        Booking.objects.create(
            movie = self.movie, 
            seat = self.seat_a1, 
            user = self.user2
        )

        response = self.client.post(
            self.booking_page,
            {"seat": self.seat_a1.id},
            follow=True
        )

        # Check that the term "already booked" appears in the messages when trying to book the seat
        for message in get_messages(response.wsgi_request):
            self.assertTrue("already booked" in str(message))

    def test_same_seat_on_different_movie_succeeds(self):
        other_movie = Movie.objects.create(
            title = "Test Movie 2",
            description = "Description for Test Movie 2",
            release_date = date(2026, 10, 5),
            duration = 30
        )
        Booking.objects.create(
            movie = self.movie,
            seat = self.seat_a1, # a seat we already booked on movie 1
            user = self.user2
        )

        # Book seat on Test Movie 2
        url = reverse("book_seat", args=[other_movie.id])
        self.client.post(url, {"seat": self.seat_a1.id})

        self.assertTrue(
            Booking.objects.filter(movie=other_movie, seat=self.seat_a1).exists()
        )

class UnauthenticatedAccessTests(BookingBase):
    def test_booking_page_requires_login(self):
        response = self.client.get(self.booking_page)

        # Ensure we redirect to the login page
        self.assertRedirects(
            response,
            f"{self.login_page}?next={self.booking_page}"
        )

    def test_my_bookings_page_requires_login(self):
        response = self.client.get(self.history_page)
        self.assertRedirects(
            response,
            f"{self.login_page}?next={self.history_page}"
        )

    def test_manual_post_to_booking_page_fails(self):
        response = self.client.post(self.booking_page, {"seat": self.seat_a1.id})
        # Ensure that the status code returned is 302 
        self.assertEqual(response.status_code, 302)

    def test_manual_api_booking_is_rejected(self):
        api = APIClient()
        response = api.post(
            "/api/bookings/",
            {
                "movie": self.movie.id,
                "seat": self.seat_a2.id
            },
            format="json"
        )
        self.assertEqual(response.status_code, 403)