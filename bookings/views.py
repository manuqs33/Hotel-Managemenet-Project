from rest_framework.response import Response
from rest_framework import status
from .models import Booking, Room
from .serializers import BookingSerializer, RoomSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import DjangoObjectPermissions


class BookingViewSet(ModelViewSet):

    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    """ permission_classes = [DjangoObjectPermissions] """

    """ def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data) """


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

