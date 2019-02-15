from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post 
from django.views.generic import ListView, DetailView
from blog.models import Category

# def index(request):
#     if request.method == 'GET':
#         return render(request, 'blog/index.html', {})


class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug_)
