from django.db import models

# Create your models here.


class DogBoarding(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)  # for example 99.90 per night
    capacity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='boarding_images/', null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

