
from django.contrib import admin
from .models import Bakery


class BakeryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'hp',
        'operated_date',
        'address'
    )
    search_fields = ('name', 'operated_date', 'address')


admin.site.register(Bakery, BakeryAdmin)
