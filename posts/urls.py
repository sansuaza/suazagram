""" Posts URLs"""

from django.urls import path

from posts import views
urlpatterns = [
    path(
        route ='',
        view =views.PostsFeedView.as_view(), 
        name='feed'
        ),

    path(
        route ='new/',
        view= views.CreatePostView.as_view(), 
        name ='create'
        ),

    path(
        route = 'posts/<str:id>',
        view = views.PostsDetailView.as_view(), 
        name = 'detail'
        ),
]
