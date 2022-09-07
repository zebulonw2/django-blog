from .models import Post
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_protect


@csrf_protect
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title", "text",
        ]
