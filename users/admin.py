from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'date_of_birth', 'date_of_joining')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Favorites', {'fields': ('favorite_books', 'favorite_genres', 'read_books')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'date_of_birth', 'date_of_joining', 'is_staff')
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)