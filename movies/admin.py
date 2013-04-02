from django.contrib import admin
from movies import models

admin.site.register(models.Genre)
admin.site.register(models.Actor)
admin.site.register(models.Movie)
#admin.site.register(models.Cast)
