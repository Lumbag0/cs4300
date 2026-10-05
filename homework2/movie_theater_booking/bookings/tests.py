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
            release_date = date(2026, 1, 1),
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
    