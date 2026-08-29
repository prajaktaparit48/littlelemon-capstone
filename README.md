# Little Lemon Capstone

Django REST Framework API for restaurant table bookings and menu management.

## Features / rubric coverage

- Django serves static HTML at `/` (see `templates/index.html`).
- Backend connects to MySQL via `django.db.backends.mysql` (see `littlelemon/settings.py`).
- Menu API: `/api/menu/` (list/create/retrieve/update/delete).
- Booking API: `/api/bookings/` (auth required).
- User registration: `/api/registration/`, token login: `/api/token-auth/`.
- Unit tests: `restaurant/tests.py`.
- Testable with Insomnia (or curl/Postman) using Token authentication.

## Setup

1. Create and activate a virtual environment, then install dependencies:

   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Configure the database. For MySQL (required for submission), create the
   database and set environment variables:

   ```
   mysql -u root -p -e "CREATE DATABASE littlelemon;"

   export DB_NAME=littlelemon
   export DB_USER=root
   export DB_PASSWORD=yourpassword
   export DB_HOST=127.0.0.1
   export DB_PORT=3306
   ```

   To quickly try the project without MySQL installed, use SQLite instead:

   ```
   export DB_ENGINE=sqlite
   ```

3. Run migrations and create a superuser:

   ```
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Start the server:

   ```
   python manage.py runserver
   ```

5. Run the test suite:

   ```
   python manage.py test
   ```

## Testing the API with Insomnia

1. `POST /api/registration/` with `{"username": "...", "email": "...", "password": "..."}`
   to create a user (response includes a token), or
   `POST /api/token-auth/` with `{"username": "...", "password": "..."}` to log in an
   existing user.
2. Add header `Authorization: Token <token>` to authenticated requests.
3. `GET /api/menu/` works without a token; `POST /api/menu/` needs one.
4. `GET`/`POST` `/api/bookings/` always needs a token.

## Git

```
git init
git add .
git commit -m "Little Lemon capstone: menu & booking API"
git remote add origin <your-github-repo-url>
git push -u origin main
```
