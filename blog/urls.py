from django.conf.urls import url
from blog.views import PostsListView, PostDetailView

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
]