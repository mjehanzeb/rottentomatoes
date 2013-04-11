# This will house all operations related to RottenTomatoes API

import requests

API_KEY = 'v42gy6vz74y2xjaxe7gf92k5' # Insert Here RottenTomatoes API key
API_BASE_URL = 'http://api.rottentomatoes.com/api/public/v1.0/'
PAGE_LIMIT = 5

def get_movies(search_term):

	search_url = API_BASE_URL + 'movies.json'
	params = {
				'apikey': API_KEY,
				'page_limit': PAGE_LIMIT,
				'q': search_term,
	}
		
	response = requests.get(search_url, params=params)

	movies = []
		
	if response.status_code == requests.codes.ok:
		response = response.json()
		if response['movies']:
			movies = response['movies']
	
	return movies

def get_movie_detail(movie_id):

	movie_url = API_BASE_URL + 'movies/%s.json' %movie_id
	params = {
				'apikey': API_KEY,
	}

	response = requests.get(movie_url, params=params)
	movie = {}
		
	if response.status_code == requests.codes.ok:
		movie = response.json()
	
	return movie

def save_movie(movie):
	
	from django.utils import simplejson
	from movies import models

	movie_object = models.Movie() # Initialize movie object
	for field in models.Movie._meta.fields:
		if field.name != 'id':
			setattr(movie_object, field.name, movie.get(field.name, None))

		if isinstance(movie.get(field.name, None), dict):
			setattr(movie_object, field.name, simplejson.dumps(movie.get(field.name, None)))

		if movie.get('id', None):
			setattr(movie_object, 'movie_id', movie.get('id', None))
		
	m = movie_object.save()
	
	for genre in movie['genres']:
		genre_object, created = models.Genre.objects.get_or_create(name=genre)
		movie_object.genres.add(genre_object)

	for cast in movie['abridged_cast']:
		actor_object, created = models.Actor.objects.get_or_create(name=cast['name'])
		movie_object.actors.add(actor_object)
	
def movie_mixin(cost, genre):

	from random import choice
	
	from movies import models

	genre_liquor_map = {'Animation' : 'Non-Alcoholic', 'Classics' : 'Wine', 'Comedy' : 'Lager', 'Documentary' : 'Beer'}
	liquor_type = genre_liquor_map.get(genre, 'Beer')  # Make Beer as default category

	movie_list = lcbo_products = []
	data = {}

	lcbo_api_url = 'http://lcboapi.com/products?per_page=100';
	response = requests.get(lcbo_api_url)

	if response.status_code == requests.codes.ok and liquor_type:
		lcbo_response = response.json()
		for lcbo_product in lcbo_response['result']:
			if (lcbo_product['price_in_cents'] <= cost * 100) and (liquor_type == lcbo_product['primary_category'] or liquor_type == lcbo_product['secondary_category']):
				lcbo_products.append({'lcbo_product_name': lcbo_product['name'],
									'price': lcbo_product['price_in_cents'] / 100,
									})

		#pick a random product and movie
		if lcbo_products:
			lcbo_product = choice(lcbo_products)

			movie_list = models.Movie.objects.filter(genres__name=genre).values()
			if movie_list:
				movie = choice(movie_list)
				data = dict(movie.items() + lcbo_product.items())

	return data