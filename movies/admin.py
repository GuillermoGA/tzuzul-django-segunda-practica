from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'synopsis', 'image', 'release_date')
    list_display = ('__str__', 'slug')

admin.site.register(Movie, MovieAdmin)
