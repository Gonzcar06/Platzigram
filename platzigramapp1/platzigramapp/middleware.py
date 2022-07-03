"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:##un middleware se llama automaticamente despues de un GET
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):##documentacion 
        """Middleware initialization."""
        self.get_response = get_response####

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:###verifica si un usuario esta logeado PROPIEDAD DEL MIDELWARE //si el usuario no es anonimo
            profile = request.user.profile ##traemos el perfil , una forma de traer los onetoonefield
            if not profile.picture or not profile.biography:##si no existe picture ni briography nos redirecciona a update_profile
                if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:#si request,path no esta en ninguna de las dos opciones si no seguira ejecutandose el middleware
                    return redirect('users:update_profile')

        response = self.get_response(request)
        return response