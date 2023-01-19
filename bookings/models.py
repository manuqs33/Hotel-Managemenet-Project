from django.db import models

# Create your models here.
class Booking(models.Model):

    PAYMENT_CHOICES = [
        ('CC', 'credit_card'),
        ('C', 'cash'),
        ('T', 'transfer')
    ]
    STATUS_OPTIONS = [
        ('Pe', 'pending'),
        ('Pa', 'payed'),
        ('De', 'deleted')
    ]

    room_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    client_name = models.CharField(max_length=255)
    client_dni = models.IntegerField()
    price = models.IntegerField()
    payment_method = models.CharField(
        max_length=255,
        choices=PAYMENT_CHOICES,
        default='CC'
    )
    status_code = models.CharField(
        max_length=255,
        choices=STATUS_OPTIONS,
        default='Pe'
    )

    class META:
        verbose_name = "Reserva"

    def __str__(self):
        return "Reserva " + str(self.pk)