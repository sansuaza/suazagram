

from django.urls import path
from suazagram import views


urlpatterns = [
    path('hello-world/', views.hello_World),
    path('sorted',views.sorted),
    path('hi/<str:name>/<int:age>/',views.hi)
]
