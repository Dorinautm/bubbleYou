from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.header, name='header'),
    path('about/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('contacts/', views.contacts, name='contacts'),
    path('posts/', views.posts, name='posts')
]