from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic.edit import CreateView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Book, Category, Comment
from .forms import CommentForm



#def get_home_page(request):
#    return render(request, 'index.html')

class HomePage(generic.ListView):
    queryset = Book.objects.order_by('title')
    template_name = 'index.html'

class AboutUsPage(generic.ListView):
    queryset = Book.objects.order_by('title')
    template_name = 'aboutus.html'


class FinanceBookList(generic.ListView):
    queryset = Book.objects.order_by('title').filter(category=34)
    template_name = "finance.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.POST)
        return context

    
class CommentBookList(CreateView):
    
    model = Comment
    form_class = CommentForm
    success_url = 'https://8000-claudiocruz-devbooks-zthg18alnnz.ws-eu77.gitpod.io/finance/'

    def form_valid(self, form):
        form.instance.name = self.request.user.username
        book = get_object_or_404(Book, id=self.kwargs['pk'])
        form.instance.title = book
        form.save()
        return super().form_valid(form)


class BiographyBookList(generic.ListView):
    queryset = Book.objects.order_by('title').filter(category=38)
    template_name = "biography.html"

    def get_comment_data(self, **kwargs):
        context = super().get_comment_data(**kwargs)
        context['comments'] = Comment.objects.filter(approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.GET)
        return context


class HealthBookList(generic.ListView):
    queryset = Book.objects.order_by('title').filter(category=36)
    template_name = "health.html"

    def get_comment_data(self, **kwargs):
        context = super().get_comment_data(**kwargs)
        context['comments'] = Comment.objects.filter(approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.GET)
        return context


class SpiritualBookList(generic.ListView):
    queryset = Book.objects.order_by('title').filter(category=35)
    template_name = "spiritual.html"

    def get_comment_data(self, **kwargs):
        context = super().get_comment_data(**kwargs)
        context['comments'] = Comment.objects.filter(approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.GET)
        return context
    

class LeadershipBookList(generic.ListView):
    queryset = Book.objects.order_by('title').filter(category=37)
    template_name = "leadership.html"

    def get_comment_data(self, **kwargs):
        context = super().get_comment_data(**kwargs)
        context['comments'] = Comment.objects.filter(approved=True).order_by('-created_on')
        context['comment_form'] = CommentForm(self.request.GET)
        return context


class BookLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Book, book.title )
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('finance-book-list', args=[ book.title ]))