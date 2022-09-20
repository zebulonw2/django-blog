from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import PostForm
from django.shortcuts import render, redirect


class PostList(ListView):
    model = Post
    template_name = "blogging/list.html"


class PostDetail(DetailView):
    model = Post
    template_name = "blogging/detail.html"

    def get_queryset(self):
        return Post.objects.exclude(published_date__exact=None)


def add_post(request):
    context = {}
    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("blog_index")
        else:
            print(form.errors)
    context["form"] = form
    return render(request, "blogging/add.html", context)
