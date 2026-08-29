Little Lemon Capstone - API paths for peer review
==================================================

Home page (static HTML):
/

Menu API (GET is open to everyone; POST/PUT/DELETE require a token):
/api/menu/
/api/menu/<id>/

Table booking API (requires an auth token for all methods):
/api/bookings/
/api/bookings/<id>/

User registration:
/api/registration/
  POST body: {"username": "...", "email": "...", "password": "..."}
  Returns the new user plus an auth token.

Obtain auth token (login):
/api/token-auth/
  POST body: {"username": "...", "password": "..."}
  Returns {"token": "..."}

To test protected endpoints in Insomnia, add this header once you have a
token:
  Authorization: Token <your-token-here>

Admin site:
/admin/
