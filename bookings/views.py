from rest_framework import generics
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



class BookingViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

