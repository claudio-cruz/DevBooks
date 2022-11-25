from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'category')


@admin.register(models.Book)
class BookAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'category', 'slug', 'author', 'status')
    list_filter = ('category', 'author', 'status')
    search_fields = ('title', 'category')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'title', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'title', 'name')
    search_fields = ('name', 'body', 'title')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
