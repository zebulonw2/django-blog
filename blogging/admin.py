from django.contrib import admin
from blogging.models import Post, Category


class CategoryInLine(admin.TabularInline):
    model = Post.categories.through


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [
        CategoryInLine,
    ]
    fields = ("title", "text", "author", "published_date")
    filter_horizontal = ("categories",)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
