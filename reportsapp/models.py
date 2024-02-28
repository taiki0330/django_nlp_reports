from django.db import models
from django.utils import timezone

# Create your models here.
class GenreModel(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class CrimeModel(models.Model):
    genre = models.ForeignKey(GenreModel, on_delete=models.CASCADE)
    crime_name = models.CharField(max_length=100)
    crime_name_second = models.CharField(max_length=100, null=True, blank=True)
    crime_start_datetime = models.DateTimeField(null=True, blank=True, default=timezone.now)
    crime_end_datetime = models.DateTimeField(null=True, blank=True, default=timezone.now)
    crime_place = models.CharField(max_length=100)
    crime_fact = models.TextField()

    def __str__(self):
        return self.crime_name


class SuspectModel(models.Model):
    crime = models.ForeignKey(CrimeModel, on_delete=models.CASCADE)
    honseki = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name



class VictimModel(models.Model):
    crime = models.ForeignKey(CrimeModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name