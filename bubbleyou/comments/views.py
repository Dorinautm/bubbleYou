from django.utils import timezone

from django.shortcuts import render
from .models import Post

def post_list(request):
    post= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'comments/post_list.html', {'post': post})


