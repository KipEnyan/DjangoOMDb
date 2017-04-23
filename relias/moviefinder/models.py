from django.db import models

# Create your models here.
class Movie(models.Model):
    Title = models.TextField()
    Year = models.CharField(max_length=15, blank=True, null=True)
    Rated = models.CharField(max_length=15, blank=True, null=True)
    Released = models.CharField(max_length=255, blank=True, null=True)
    Runtime = models.CharField(max_length=255, blank=True, null=True)
    Genre = models.TextField(blank=True, null=True)
    Director = models.TextField(blank=True, null=True)
    Writer = models.TextField(blank=True, null=True)
    Actors = models.TextField(blank=True, null=True)
    Plot = models.TextField(blank=True, null=True)
    Language = models.TextField(blank=True, null=True)
    Country = models.TextField(blank=True, null=True)
    Awards = models.TextField(blank=True, null=True)
    Poster = models.URLField(blank=True, null=True)
    Ratings = models.TextField(blank=True, null=True)
    Metascore = models.PositiveSmallIntegerField(blank=True, null=True)
    imdbRating = models.FloatField(blank=True, null=True)
    imdbVotes = models.CharField(max_length=255, blank=True, null=True)
    imdbId = models.CharField(max_length=15, blank=True, null=True)
    Type = models.TextField(blank=True, null=True)
    DVD = models.CharField(max_length=255, blank=True, null=True)
    BoxOffice = models.CharField(max_length=255, blank=True, null=True)
    Production = models.TextField(blank=True, null=True)
    Website = models.URLField(blank=True, null=True)
    Response = models.NullBooleanField(blank=True, null=True)

    def __str__(self):
        return self.Title