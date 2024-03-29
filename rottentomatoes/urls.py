from django.conf.urls import patterns, include, url
from movies import views
from moviesmixin import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rottentomatoes.views.home', name='home'),
    # url(r'^rottentomatoes/', include('rottentomatoes.foo.urls')),

    url(r'^$', 'movies.views.index'),
    url(r'^movie/(\d+)/$', 'movies.views.movie'),
    url(r'^moviesmixin/$', 'moviesmixin.views.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
