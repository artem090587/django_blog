from django.contrib import admin
from .models import Category, Post, Tag, Comment
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Category


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ['title', 'category', 'description', 'img', 'text', 'slug', 'published_date', 'publishTrue']
    list_filter = ('publishTrue', 'published_date', 'category')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('text',)


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
        