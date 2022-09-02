from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostList(ListView):
    model = Post
    template_name = "blogging/list.html"


class PostDetail(DetailView):
    model = Post
    template_name = "blogging/detail.html"

    def get_queryset(self):
        return Post.objects.exclude(published_date__exact=None)
