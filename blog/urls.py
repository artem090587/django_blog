from django.conf.urls import url
from django.urls import path, re_path, include
from . import views
from blog.views import PostsListView, PostDetailView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'blog'

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='posts-list'),
    url(r'^accounts/', include('allauth.urls')),
    re_path(r'^(?P<slug>\w+)/$', PostsListView.as_view(), name='posts-list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),

    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)