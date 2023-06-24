"""
This module provides the views for the application.

It includes the views for HomePage, AboutUsPage, FinanceBookList,
BiographyBookList, HealthBookList, SpiritualBookList, SpiritualBookList,
LeadershipBookList, CommentBookList, and BookLike views.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views import generic, View
from .models import Book, Comment
from .forms import CommentForm
from django.contrib import messages
from django.db.models import Count


class HomePage(generic.ListView):
    """
    View for the home page displaying a list of all books and book comments.
    """

    queryset = Book.objects.annotate(
        like_count=Count('likes')).order_by('-like_count')
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """Retrieve additional context data for the home page."""
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.POST)
        return context


class AboutUsPage(generic.ListView):
    """View for the about us page."""

    queryset = Book
    template_name = 'aboutus.html'


class FinanceBookList(generic.ListView):
    """View for displaying a list of finance books."""

    queryset = Book.objects.annotate(like_count=Count(
        'likes')).order_by('-like_count').filter(category=34)
    template_name = "finance.html"

    def get_context_data(self, **kwargs):
        """Retrieve additional context data for the finance book list."""
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.POST)
        return context


class BiographyBookList(generic.ListView):
    """View for displaying a list of biography books."""

    queryset = Book.objects.annotate(like_count=Count(
        'likes')).order_by('-like_count').filter(category=38)
    template_name = "biography.html"

    def get_context_data(self, **kwargs):
        """Retrieve additional context data for the biography book list."""
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.GET)
        return context


class HealthBookList(generic.ListView):
    """View for displaying a list of health books."""

    queryset = Book.objects.annotate(like_count=Count(
        'likes')).order_by('-like_count').filter(category=36)
    template_name = "health.html"

    def get_context_data(self, **kwargs):
        """Retrieve additional context data for the health book list."""
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.GET)
        return context


class SpiritualBookList(generic.ListView):
    """View for displaying a list of spiritual books."""

    queryset = Book.objects.annotate(like_count=Count(
        'likes')).order_by('-like_count').filter(category=35)
    template_name = "spiritual.html"

    def get_context_data(self, **kwargs):
        """Retrieve additional context data for the spiritual book list."""
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.GET)
        return context


class LeadershipBookList(generic.ListView):
    """View for displaying a list of leadership books."""

    queryset = Book.objects.annotate(like_count=Count(
        'likes')).order_by('-like_count').filter(category=37)
    template_name = "leadership.html"

    def get_context_data(self, **kwargs):
        """Retrieve additional context data for the leadership book list."""
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.GET)
        return context


from django.contrib import messages

class CommentBookList(CreateView):
    """View for creating a new comment on a book."""

    model = Comment
    form_class = CommentForm

    success_url = '/'

    def form_valid(self, form):
        """Save the form with the user and book information."""
        form.instance.name = self.request.user.username
        book = get_object_or_404(Book, id=self.kwargs['pk'])
        form.instance.book = book
        form.save()
        messages.success(self.request, 'Your comment is waiting for approval!')
        return super().form_valid(form)

def delete_comment(request, comment_id):
    """Delete a comment and display a success message."""
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user.username == comment.name:
        comment.delete()
        messages.warning(request, 'Your comment has been deleted!')

    return redirect(request.META.get('HTTP_REFERER'))


class BookLike(View):
    """View for liking or disliking a book."""

    def post(self, request, slug, *args, **kwargs):
        """Handle the POST request for liking or disliking a book."""
        book = get_object_or_404(Book, slug=slug)
        if book.likes.filter(id=request.user.id).exists():
            book.likes.remove(request.user)
            messages.success(request, 'You successfully disliked the book!')
        else:
            book.likes.add(request.user)
            messages.success(request, 'You successfully liked the book!')

        return redirect(request.META.get('HTTP_REFERER'))


def edit_comment(request, comment_id):
    """Edit a comment and display a success message."""
    comment_edit = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment_edit)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your comment has been successfully edited!')

        return redirect('home_page')

    form = CommentForm(instance=comment_edit)
    context = {
        'form': form
    }
    return render(request, 'edit_comment.html', context)
