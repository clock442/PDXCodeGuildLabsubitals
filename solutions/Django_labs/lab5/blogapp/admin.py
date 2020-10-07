from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, BlogPost

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Image',
            {
                'fields': (
                    'image',
                ),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(BlogPost)
