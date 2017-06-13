
from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Spot(models.Model):
    last_location = models.PointField(max_length=40, null=True)
    prefered_radius = models.IntegerField(default=5, help_text="in kilometers")
    objects = models.GeoManager()

    def __str__(self):
        return self.last_location


