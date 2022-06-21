"""User admin classes"""

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#Models
from django.contrib.auth.models import User
from users.models import Profile
# Register your models here.
#admin.site.register(Profile)### hace aparecer el metodo profile en admin

@admin.register(Profile)## decora con el perfi Profile para registrar los datos
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display=('pk','user','phone_number','website','picture')
    list_display_links=('pk',)##redirecciona a donde quiere ir un atributo para editar
    list_editable=('phone_number','website','picture')##para que los siguientes campos sean editables directamente
    search_fields=[
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    ]
    list_filter=["user"]

    fieldsets=(###sirve para reorganizar los campos de llenado de un atributo despues del display
        ('Profile',{
            'fields':(('user','picture'),),
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

    readonly_fields=('created','modified')###para acceder al detalle de un objeto sin poder editar

#################################
###HACE QUE EL MODELO USER POR DEFECTO; AL AGREGAR UN NUEVO USUARIO TMB SE PUEDAN AGREGAR LOS DEMAS CAMPOS
###EBSITE, BIOGRAPHY, PHONE NUMBER, PICTURE ETC ETC
class ProfileInline(admin.StackedInline):###DCOUMENTACION TAL CUAL DICE
    """Profile in-line admin for users."""
    model=Profile
    can_delete=False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInline,)
    list_display=(###podemos acceder a los parametros de USER que estamos usando de django por defecto
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
####################################