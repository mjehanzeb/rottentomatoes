from django.db import models
import datetime
from django.utils import timezone

class Actor(models.Model):
 
    name = models.CharField(max_length=100)

    def __unicode__(self):
		return self.name	
 
class Genre(models.Model):
     
    name = models.CharField(max_length=100)

    def __unicode__(self):
		return self.name	

 
class Movie(models.Model):
 
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    synopsis = models.TextField(blank=True, null=True)
    year = models.IntegerField()
    mpaa_rating = models.CharField(max_length=2)
    runtime = models.IntegerField()
    release_date_theater = models.DateField(blank=True, null=True)
    release_date_dvd = models.DateField(blank=True, null=True)
    poster_thumbnail = models.CharField(max_length=255, null=True)
    poster_profile = models.CharField(max_length=255, null=True)
    poster_detailed = models.CharField(max_length=255, null=True)
    poster_original = models.CharField(max_length=255, null=True)

    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)


    def __unicode__(self):
		return self.title		


"""class Cast(models.Model):

	actor = models.ForeignKey(Actor)
	movie = models.ForeignKey(Movie)
	characters = models.CharField(max_length=100)

	def __unicode__(self):
		return self.characters	
"""