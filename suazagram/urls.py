
#Django

from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from suazagram import views as local_views
from posts import views as post_views
from users import views as users_views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello-world/', local_views.hello_World, name='hello-world'),
    path('sorted',local_views.sorted, name='sort'),
    path('hi/<str:name>/<int:age>/',local_views.hi, name='hi'),

    path('posts/', post_views.list_posts, name='feed'),

    path('users/login/', users_views.login_view, name='login')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

