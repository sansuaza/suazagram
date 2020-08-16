from django.contrib import admin
from posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ( 'user','title', 'photo')
    list_display_links = ( 'user', 'photo')

    """
    info's grops
    """

    fieldsets = (
        ('User',{
            'fields': ( 'user',)
        }),
        ('Post info',{
            'fields': ('title', 'photo',)
        })
    )