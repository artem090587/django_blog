from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post 
from django.views.generic import ListView, DetailView

# def index(request):
#     return HttpResponse('<h3>Hello from Django!</h3>')

# def index(request):
#     if request.method == 'GET':
#         return render(request, 'blog/index.html', {})


class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
