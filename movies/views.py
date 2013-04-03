
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from movies import models
from movies import api

def index(request):

	movie_list = [] # Movie list 
	
	q = request.GET.get('q', '')

	if q:
		# First we'll search in our local database
		# In case we don't find record in our db then we'll make api call to RottonTomatoes
		try:
			movie_list = [models.Movie.objects.get(title=q).format_movie()]
		except models.Movie.DoesNotExist:
			movie_list = api.get_movies(q)
			api_result = True

	context = {'q': q, 'movie_list': movie_list}

	return render(request, 'movies/index.html', context)

def movie(request, movie_id):

	if movie_id:

		try:
			movie = models.Movie.objects.get(movie_id=movie_id).format_movie()
		except models.Movie.DoesNotExist:
			movie = api.get_movie_detail(movie_id)
			api.save_movie(movie)
			api_result = True

		context = {'movie' : movie}
	
		return render(request, 'movies/movie.html', context)

	return HttpResponseRedirect('/')