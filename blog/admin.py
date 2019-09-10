from django.contrib import admin

from .models import Category, Post, Tag, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description','text', 'slug', 'published_date', 'publishTrue']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Tag


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'text', 'created_date']

    class Meta:
        model = Comment