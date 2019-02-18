from django.conf.urls import url
from django.urls import path
from . import views
from blog.views import PostsListView, PostDetailView


app_name = 'blog'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', PostsListView.as_view(), name='posts-list'),
    # url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    # path('<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]