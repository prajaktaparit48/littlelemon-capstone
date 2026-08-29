from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MenuViewSet, BookingViewSet, RegistrationView

router = DefaultRouter()
router.register(r'menu', MenuViewSet, basename='menu')
router.register(r'bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('', include(router.urls)),
]
