from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


@admin.register(models.Book)
class BookAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'category', 'slug', 'author', 'status')
    list_filter = ('category', 'author', 'status')
    search_fields = ('title', 'category')

admin.site.register(models.Category)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'book', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'book', 'name')
    search_fields = ('name', 'body', 'book')

