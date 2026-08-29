"""littlelemon URL configuration."""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Serves static HTML content for the site's home page.
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    path('admin/', admin.site.urls),

    # Menu + Booking APIs, registration, etc.
    path('api/', include('restaurant.urls')),

    # Token auth endpoint for Insomnia: POST username/password -> {"token": "..."}
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
]
