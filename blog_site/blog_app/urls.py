from django.urls import path, re_path
from django.conf.urls import include
from blog_app import views

urlpatterns = [
    re_path(r'^about/$', views.AboutView.as_view(), name = 'about'),
    re_path(r'^$', views.PostListView.as_view(), name = 'post_list'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name = 'post_detail'),
    re_path(r'^post/new/$', views.CreatePostView.as_view(), name = 'post_new'),
    re_path(r'^post/(?P<pk>\d+)/update/$', views.UpdatePostView.as_view(), name = 'post_update'),
    re_path(r'^post/(?P<pk>\d+)/delete/$', views.DeletePostView.as_view(), name = 'post_delete'),
    re_path(r'^drafts/$', views.DraftListView.as_view(), name = 'post_draft_list'),

]
