"""User views."""

#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views#PARA USAR EL LOGIN Y EL LOGOUT
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

#MODELS
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#FORMS
from users.forms import ProfileForm,SignupForm

#LoginRequiredMixin funciona como una login_requiered
class UserDetailView(LoginRequiredMixin, DetailView):
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

######################################################################################
#@login_required
#def update_profile(request):
#    """Update a user's profile view."""
#    profile = request.user.profile
#    if request.method == 'POST': #para usar un formulario de django si esta en POST, osea enviando datos
#        form = ProfileForm(request.POST, request.FILES)#los archivos no vienen en el post sino dentro de FILES
#        if form.is_valid():#condicion es si el formulario es valido
#            data= form.cleaned_data

#            profile.website=data['website']#ingresando los datos pedidos en el formulario
#            profile.phone_number=data['phone_number']
#            profile.biography=data['biography']
#            profile.picture=data['picture']
#            profile.save()
            
#            url = reverse('users:detail', kwargs={'username':request.user.username}) #envia a detail el argumento que recibe
#            return redirect(url)#gracias al redirect no vuelve a reenviar los datos cargados
                                           
#    else:
#        form = ProfileForm()

#    return render(#render es parte de los views , para que redireccione a un template, ya sea con parametros o no
#        request=request,
#        template_name='users/update_profile.html',
#        context={
#            'profile': profile,#paso el profile
#            'user':request.user,#paso el user
#            'form':form,
#        }
#    )
########lo mismo abajo pero en clases
class UpdateProfileView(LoginRequiredMixin, UpdateView): 
    """User detail view."""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website','biography','phone_number','picture']

    def get_object(self):#sobreescribiendo el metodo get_object
        """Return user's profile."""
        return self.request.user.profile
    def get_success_url(self):
        """Return to user's profile."""
        username=self.object.user.username
        return reverse('users:detail', kwargs={'username':username})
##################################################################################

##################################################################################
#def login_view(request):
#    """Login view"""
#    if request.method =='POST':
#        username = request.POST['username']####campos a auntenticar por POST
#        password = request.POST['password']####

#        user=authenticate(request,username=username,password=password)##autentica si coinciden con la bse de datos
#        if user:
#            login(request,user)#esto hace la magia por  nosotros para entrar al login , documentacion DJANGO
#            return redirect('posts:feed')#redirecciona a la url feed
#        else:
#            return render(request, 'users/login.html',{'error':'Invalid username and password'})##retorna erro de mensajhe
#    return render(request,'users/login.html')##redirecciona al login denuevo
#####LO MISMO PERO EN CLASES, DEMASIADO INCREIBLE XD
class LoginView(auth_views.LoginView):#DOCUMENTACION
    """Login view."""
    redirect_authenticated_user = True
    template_name = 'users/login.html'
##################################################################################

##################################################################################
#@login_required
#def logout_view(request):##vista logout para salir de sesion y redireccionar denuevo a login
#    """Logout a user."""
#    logout(request)
#    return redirect('users:login')
#####LO MISMO PERO EN CLASES
class LogoutView(LoginRequiredMixin, auth_views.LogoutView):#DOCUMENTACION
    """Logout view."""

    template_name = 'users/logged_out.html'
##################################################################################



#####################################################
#def signup(request):
#    """Sign up view."""
#    if request.method =='POST':
#        form = SignupForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('users:login')
#    else:
#        form = SignupForm()
#    return render(
#        request=request,
#        template_name='users/signup.html',
#        context={'form':form}
#    )
####LO MISMO PERO EN CLASES
class SignupView(FormView):#mas documentancion
                    #LoginRequiredMixin para la sesion activa
    """Sign up view."""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
#######################################################