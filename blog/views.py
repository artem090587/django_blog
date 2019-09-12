from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post, Comment 
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Category, Tag


class PostsListView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'blog/post_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        if self.kwargs.get('slug') == 'all':
            return self.model.objects.filter(publishTrue__exact=True)
        return self.model.objects.filter(tags__slug=self.kwargs.get('slug'),
                                         publishTrue__exact=True)


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

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