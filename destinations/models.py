from django.db import models

class Destination(models.Model):
    place_name = models.CharField(max_length=100)
    weather = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    google_map_link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.place_name
    
    class Meta:
        db_table='places'
