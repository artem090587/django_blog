from django.contrib import admin

from .models import Category, Post, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'slug', 'published_date', 'publishTrue']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Post

