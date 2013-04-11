
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from movies import models
from movies import api

def index(request):

	data = [] # Movie list 
	context = {}
	
	cost = request.GET.get('cost', '')
	genre = request.GET.get('genre', '')

	context['cost'] = cost
	context['genre_selected'] = genre
	context['genre_list'] = models.Genre.objects.all().order_by('name')

	if cost and genre:
		data = api.movie_mixin(float(cost), genre)

	context['data'] =  data

	return render(request, 'movies/moviesmixin.html', context)