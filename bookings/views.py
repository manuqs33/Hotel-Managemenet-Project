from django.http import JsonResponse
from rest_framework import status
from .models import Booking, Room
from .serializers import BookingSerializer, RoomSerializer
from rest_framework.viewsets import ModelViewSet

class BookingViewSet(ModelViewSet):

    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    http_method_names = ['get', 'post', 'put']

    def create(self, request, *args, **kwargs):
        data = request.data
        # Validate that end_date is after start date
        if data['start_date'] > data['end_date']:
            return JsonResponse({'message': 'The dates are not correct. The booking should end after the start date'})
        # Validate if the room is free. It ensures the new booking doesn't overlap
        # with pending or payed reservations in the same time period.
        else:
            booking_list = Booking.objects.filter(room=data['room']).exclude(status_code='DE')
            for booking in booking_list:
                if data['end_date'] >= str(booking.start_date) and str(booking.end_date) >= data['start_date']:
                    return JsonResponse({'message': 'The room is already booked in some of the selected days'})
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        data = request.data
        # Same validations for update, except it excludes itelf when considering date overlaps
        if data['start_date'] > data['end_date']:
            return JsonResponse({'message': 'The dates are not correct. The booking should end after the start date'})
        else:
            booking_list = Booking.objects.filter(room=data['room']).exclude(status_code='DE').exclude(id=kwargs['pk'])
            for booking in booking_list:
                if data['end_date'] >= str(booking.start_date) and str(booking.end_date) >= data['start_date']:
                    return JsonResponse({'message': 'The room is already booked in some of the selected days'})
        return super().update(request, *args, **kwargs)



class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    http_method_names = ['get']

