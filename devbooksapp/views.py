from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views import generic, View
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
        context['comment_form'] = CommentForm(self.request.GET)
        return context

    #def add_comment(request):
    #    if request.method == 'POST':
    #        book = get_object_or_404(queryset, id=Book_id)
    #        form  = CommentForm(request.POST)
    #        if form.is_valid():
    #            form.save()
    #            return redirect('FinanceBookList')
    
class CommentBookList(CreateView):
    def post_comment(request):

        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
            else:
                comment_form = CommentForm()

            return redirect('FinanceBookList')

        


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