from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    #add the following method in Menu class
    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name=models.CharField(max_length=255)
    no_of_guests=models.IntegerField()
    booking_date=models.DateField()
