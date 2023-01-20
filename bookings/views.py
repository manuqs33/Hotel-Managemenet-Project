from rest_framework.response import Response
from rest_framework import status
from .models import Booking, Room
from .serializers import BookingSerializer, RoomSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import DjangoObjectPermissions


class BookingViewSet(ModelViewSet):

    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    http_method_names = ['get', 'post', 'put']


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    http_method_names = ['get']

