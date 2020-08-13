from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from users.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = ('user__email', 'user__username', 'user__last_name', 'phone_number')
    list_filter = ('created','modified','user__is_active','user__is_staff')


    """ agrupa la informacion en secciones """
    fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),)
        }),
        ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('biography'),
            )
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        })
    )
    readonly_fields = ('created','modified')
"""
Une los modelos de usuario y perfil para no tener que 
crear un usuario para asociarlo con un perfil
"""

"""En este metodo se relaciona con el modelo (profile)"""
class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

"""Elimina el usuario registrado solo, y agrega el usuario con el profile"""
admin.site.unregister(User)
admin.site.register(User,UserAdmin)