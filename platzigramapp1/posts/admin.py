from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin


#Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Profile admin."""
    list_display=('pk','user','profile','title','photo',)
    list_display_links=('pk','user')##redirecciona a donde quiere ir un atributo para editar
    list_editable=('title','photo')
    search_fields=(
        'user__username',
        'title'
    )
    list_filter=["user"]
  