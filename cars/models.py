from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

class Car(models.Model):
    buyer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    car_model = models.CharField(max_length=60, blank=False, null=False)
    car_brand = models.CharField(max_length=200, blank=False, null=False)
    car_price = models.PositiveIntegerField(blank=False, null=False)
    is_bought = models.BooleanField(blank=False, null=False)
    buy_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.car_model
    def get_absolute_url(self):
        return reverse('details', args=[self.id])