from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post, Comment 
from django.views.generic import ListView, DetailView
from blog.models import Category
from .forms import CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)