"""Posts views."""

#Django
from django.contrib.auth.decorators import login_required ##sirve para acceder si esta logiado
from django.shortcuts import render, redirect

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post



@login_required##para saber si se logio y poder mantener la sesion activa
def list_posts(request):
    """List existing posts."""
    posts=Post.objects.all().order_by('-created')#trae todos los post ordenados alreves
    return render(request,'posts/feed.html', {'posts':posts})


@login_required
def create_post(request):
    """Create new post view."""
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)#se coloca FILE por que se mandara una foto
        if form.is_valid():#si el formulario es valido
            form.save()#la ventaja de usar modelform y automaticamente se crea un POST
            return redirect('feed')#redirecciona a feed
    else:
        form=PostForm()
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        })