from .models import Post
from django.forms import ModelForm, widgets


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = []
        widgets = {"published_date": widgets.DateTimeInput(attrs={"type": "date"})}


# todo: get datetime widget working
# todo: add categories inline to add page
