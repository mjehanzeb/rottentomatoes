
import datetime

from django.db import models
from django.utils import timezone
from django.utils import simplejson


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
    posters = models.TextField(blank=True, null=True)
    release_dates = models.TextField(blank=True, null=True)

    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)


    def __unicode__(self):
		return self.title		

    def format_movie(self):
        self.id = self.movie_id
        self.posters = dict(simplejson.loads(self.posters))
        self.release_dates = dict(simplejson.loads(self.release_dates))

        return self