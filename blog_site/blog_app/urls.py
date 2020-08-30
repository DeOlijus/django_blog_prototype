from django.urls import re_path
from blog_app import views

urlpatterns = [
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
    re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    re_path(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/update/$', views.UpdatePostView.as_view(), name='post_update'),
    re_path(r'^post/(?P<pk>\d+)/delete/$', views.DeletePostView.as_view(), name='post_delete'),
    re_path(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.approve_comment_on_post, name='approve_comment_on_post'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.remove_comment_on_post, name='remove_comment_on_post'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.publish_post, name='post_publish'),

]
