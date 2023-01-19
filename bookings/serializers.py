from .models import Booking
from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = [
            'room_id',
            'start_date',
            'end_date',
            'client_name',
            'client_dni',
            'price',
            'payment_method',
            'status_code'
        ]