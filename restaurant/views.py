from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, RegistrationSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    Anyone can view the menu (GET). Only authenticated users can
    create/update/delete menu items.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    """
    Table bookings. Requires an authenticated user (token) for every
    action, including listing/creating a reservation.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegistrationView(APIView):
    """
    POST /api/registration/ with {"username", "email", "password"}
    creates a new user and returns an auth token.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'token': token.key,
            },
            status=status.HTTP_201_CREATED,
        )
