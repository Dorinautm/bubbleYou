from django.urls import path
from . import views as c

urlpatterns = [
    path('', c.post_list, name='post_list'),

]