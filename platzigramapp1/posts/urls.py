"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [

    path(
        route='',
        #view=views.list_posts,
        view=views.PostsFeedView.as_view(),
        name='feed'),

    path(
        route='posts/new/',
        #view=views.create_post,
        view=views.CreatePostView.as_view(),
        name='create_post'),

    path(
        route ='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'),
]