"""Posts views."""

#Django
from django.contrib.auth.decorators import login_required ##sirve para acceder si esta logiado
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DetailView,ListView#documentacion

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):#vista basada en clases
    """Return all published posts."""
    template_name='posts/feed.html'
    model=Post
    ordering=('-created',)
    paginate_by=30#para la paginacion
    context_object_name = 'posts'

#@login_required##para saber si se logio y poder mantener la sesion activa
#def list_posts(request):
#    """List existing posts."""
#    posts=Post.objects.all().order_by('-created')#trae todos los post ordenados alreves
#    return render(request,'posts/feed.html', {'posts':posts})

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

############################################################################
class CreatePostView(LoginRequiredMixin, CreateView):#mas documentancion
                    #LoginRequiredMixin para la sesion activa
    """Create a new post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')#lo evalua hasta que lo necesite

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context
###########LO MISMO SOLO QUE EN CLASES
#@login_required
#def create_post(request):
#    """Create new post view."""
#    if request.method =='POST':
#        form = PostForm(request.POST, request.FILES)#se coloca FILE por que se mandara una foto
#        if form.is_valid():#si el formulario es valido
#            form.save()#la ventaja de usar modelform y automaticamente se crea un POST
#            return redirect('posts:feed')#redirecciona a feed
#    else:
#        form=PostForm()
#    return render(
#        request=request,
#        template_name='posts/new.html',
#        context={
#            'form': form,
#            'user': request.user,
#            'profile': request.user.profile
#        })
##################################################################