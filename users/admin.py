
from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'level',
        'email',
        'hp'
        )
    search_fields = ('user_id', 'level', 'email', 'hp')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group) # Admin 페이지의 GROUP 삭제

