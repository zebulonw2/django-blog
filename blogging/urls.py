from django.urls import path
from blogging.views import PostList, PostDetail

urlpatterns = [
    path("", PostList.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="blog_detail"),
]
