from django.db import models


class Room(models.Model):
    number_of_guests = models.PositiveIntegerField()
    price_per_night = models.PositiveIntegerField()

    def __str__(self):
        return "Room number " + str(self.pk)


class Booking(models.Model):

    PAYMENT_CHOICES = [
        ('CC', 'Credit_card'),
        ('CA', 'Cash'),
        ('TR', 'Transfer')
    ]
    STATUS_OPTIONS = [
        ('PE', 'Pending'),
        ('PA', 'Paid'),
        ('DE', 'Deleted')
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    client_name = models.CharField(max_length=255)
    client_identity_card = models.PositiveIntegerField()
    client_email = models.EmailField(max_length = 255)

    price = models.PositiveIntegerField()
    payment_method = models.CharField(
        max_length=255,
        choices=PAYMENT_CHOICES,
        default='CC'
    )
    status_code = models.CharField(
        max_length=255,
        choices=STATUS_OPTIONS,
        default='PE'
    )

    def __str__(self):
        return "Booking number " + str(self.pk)

