from django.contrib import admin
from django.urls import path
from home import views 


urlpatterns = [
    path('', views.index, name="index"),
    path('campus/',views.campus, name="campus"),
    path('hall/',views.hall, name="hall"),
    path('club/',views.club, name="club"),
    path('sports/',views.sports, name="sports"),
    path('alumni/',views.alumni, name="alumni"),
    path('blog/',views.blog, name="blog"),
    path('posts/<str:id>/',views.post, name="post"),
]