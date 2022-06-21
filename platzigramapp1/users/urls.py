"""Users URLs."""

# Django
from django.urls import path

# View
from users import views


urlpatterns = [
    #POSTS
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),#sintazxis para llamar una clase desde las vistas
        #view=TemplateView.as_view(template_name='users/detail.html'),#crear una vista con template, se colocal cualquier direccion despues
        name='detail',
        ),
    #MANAGEMENT
    path(  
        route='/login/',
        view=views.login_view, 
        name='login'),
    path(
        route='/logout/',
        view=views.logout_view, 
        name='logout'),
    path(
        route='/signup/',
        view=views.signup, 
        name='signup'),
    path(
        route='me/profile/',
        view=views.update_profile, 
        name='update_profile'),
]