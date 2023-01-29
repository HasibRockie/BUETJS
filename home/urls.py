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
    path('gellery/',views.gellery,name="gellery"),
    path('blog/',views.blog, name="blog"),
    path('contact/',views.contact, name="contact"),
    path('posts/<str:id>/',views.post, name="post"),
    path('signup/',views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('profile/edit/', views.accountSettings, name="edit"),
]