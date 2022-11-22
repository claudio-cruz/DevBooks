from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book, Category, Comment
from .forms import CommentForm


def get_home_page(request):
    return render(request, 'index.html')


class FinanceBookList(generic.ListView):
    queryset = Book.objects.order_by('title').filter(category=34)
    template_name = "finance.html"

    def get_comment_data(self, **kwargs):
        context = super().get_comment_data(**kwargs)
        context['comments'] = Comment.objects.filter(approved=True).order_by('-created_on')
        
        return context


class BiographyBookList(generic.ListView):
    queryset = Book.objects.order_by('title').filter(category=38)
    template_name = "biography.html"

    def get_comment_data(self, **kwargs):
        context = super().get_comment_data(**kwargs)
        context['comments'] = Comment.objects.filter(approved=True).order_by('-created_on')
        
        return context


class HealthBookList(generic.ListView):
    queryset = Book.objects.order_by('title').filter(category=36)
    template_name = "health.html"

    def get_comment_data(self, **kwargs):
        context = super().get_comment_data(**kwargs)
        context['comments'] = Comment.objects.filter(approved=True).order_by('-created_on')
        
        return context


class SpiritualBookList(generic.ListView):
    queryset = Book.objects.order_by('title').filter(category=35)
    template_name = "spiritual.html"

    def get_comment_data(self, **kwargs):
        context = super().get_comment_data(**kwargs)
        context['comments'] = Comment.objects.filter(approved=True).order_by('-created_on')
        
        return context
    

class LeadershipBookList(generic.ListView):
    queryset = Book.objects.order_by('title').filter(category=37)
    template_name = "leadership.html"

    def get_comment_data(self, **kwargs):
        context = super().get_comment_data(**kwargs)
        context['comments'] = Comment.objects.filter(approved=True).order_by('-created_on')
        
        return context