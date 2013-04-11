from django.conf.urls import patterns, include, url
from movies import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/?$', 'movies.views.index', name='home'), 
)
