from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views
from register import views as v
from comments import views as c
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.header, name='header'),
    path('header/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('posts/', views.posts, name='posts'),
    #path('logout/', views.logout, name="registration"),
    path("signup/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    #path('', include('comments.urls')),
    path('post_list/', c.post_list, name='comments'),


]