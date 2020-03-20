from django.urls import path

from bubbleyou.bubbleyou import views

urlpatterns = [
    path('', views.index, name='index'),
]