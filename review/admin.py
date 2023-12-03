
from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'writer',
        'registered_date'
    )
    search_fields = ('title', 'content', 'writer__user_id')


admin.site.register(Review, ReviewAdmin)