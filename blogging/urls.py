from django.urls import path
from .views import PostList, PostDetail, add_post


urlpatterns = [
    path("", PostList.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="blog_detail"),
    path("add/", add_post, name="add_post"),
]
