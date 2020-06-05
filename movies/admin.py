from django.contrib import admin
from .models import Movie, MPAA_Rating, Genre

# Set basic Admin settings
admin.site.site_header = "Omni Apps Admin"
admin.site.site_title = "Omni Apps Movies Portal"
admin.site.index_title = "Welcome to Omni Apps Movies Portal"


#Register Models
admin.site.register(MPAA_Rating)
admin.site.register(Genre)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    '''Admin View for Movie'''

    list_select_related = True
    list_display = (
        'name',
        'duration',
        'get_genres_string',
        'language',
        'user_rating'
        )
    list_filter = (
        'genres',
        'language',
        'user_rating'
        )
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)