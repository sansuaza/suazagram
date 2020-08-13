

from django.urls import path
from django.contrib import admin

from suazagram import views as local_views
from post import views as post_views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello-world/', local_views.hello_World),
    path('sorted',local_views.sorted),
    path('hi/<str:name>/<int:age>/',local_views.hi),

    path('posts/', post_views.list_posts)
]
