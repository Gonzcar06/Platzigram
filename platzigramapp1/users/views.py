"""User views."""

#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

#MODELS
from django.contrib.auth.models import User
from posts.models import Post

#FORMS
from users.forms import ProfileForm,SignupForm

class UserDetailView(DetailView):
    """User detail view."""

    template_name='users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset=User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)#documentacion
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile
    if request.method == 'POST': #para usar un formulario de django si esta en POST, osea enviando datos
        form = ProfileForm(request.POST, request.FILES)#los archivos no vienen en el post sino dentro de FILES
        if form.is_valid():#condicion es si el formulario es valido
            data= form.cleaned_data

            profile.website=data['website']#ingresando los datos pedidos en el formulario
            profile.phone_number=data['phone_number']
            profile.biography=data['biography']
            profile.picture=data['picture']
            profile.save()
            
            url = reverse('users:detail', kwargs={'username':request.user.username}) #envia a detail el argumento que recibe
            return redirect(url)#gracias al redirect no vuelve a reenviar los datos cargados
                                           
    else:
        form = ProfileForm()

    return render(#render es parte de los views , para que redireccione a un template, ya sea con parametros o no
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,#paso el profile
            'user':request.user,#paso el user
            'form':form,
        }
    )

def login_view(request):
    """Login view"""
    if request.method =='POST':
        username = request.POST['username']####campos a auntenticar por POST
        password = request.POST['password']####

        user=authenticate(request,username=username,password=password)##autentica si coinciden con la bse de datos
        if user:
            login(request,user)#esto hace la magia por  nosotros para entrar al login , documentacion DJANGO
            return redirect('posts:feed')#redirecciona a la url feed
        else:
            return render(request, 'users/login.html',{'error':'Invalid username and password'})##retorna erro de mensajhe
    return render(request,'users/login.html')##redirecciona al login denuevo

@login_required
def logout_view(request):##vista logout para salir de sesion y redireccionar denuevo a login
    """Logout a user."""
    logout(request)
    return redirect('users:login')

def signup(request):
    """Sign up view."""
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form':form}
    )
