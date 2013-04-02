
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
			movie_list = models.Movie.objects.get(title=q)
		except models.Movie.DoesNotExist:
			movie_list = api.get_movies(q)

	context = {'q': q, 'movie_list': movie_list}

	#return HttpResponse("hey %r" %api.get_movies(q))
	
	return render(request, 'movies/index.html', context)

def movie(request, movie_id):

	if movie_id:

		try:
			movie = models.Movie.objects.get(movie_id=movie_id)
		except models.Movie.DoesNotExist:
			movie = api.get_movie_detail(movie_id)
			api.save_movie(movie)

		context = {'movie' : movie}
	
		return render(request, 'movies/movie.html', context)

	return HttpResponseRedirect('/')