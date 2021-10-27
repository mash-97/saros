from django.urls import path
from django.urls.resolvers import URLPattern 
from posts.views import * 

app_name = "posts"
urlpatterns = [ 
    path('', PostList.as_view(), name="post_list"),
    path('create-post', PostCreate.as_view(), name="create_post"),
    path('<slug:slug>', PostDetail.as_view(), name="post_detail"),
]