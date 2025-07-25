from django.db import models

class Booking(models.Model):
    id = models.IntegerField(primary_key=True)  # INT(11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.booking_date}"


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)  # INT(5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title