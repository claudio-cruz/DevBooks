from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Book, Category, Comment
from .forms import CommentForm
from django.contrib import messages



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
    

class CommentBookList(CreateView):
    
    model = Comment
    form_class = CommentForm
    
    if Book.category is 'finance':
        success_url = 'https://8000-claudiocruz-devbooks-gemvbskfs0w.ws-eu77.gitpod.io/finance/'
    else:
        success_url = 'https://8000-claudiocruz-devbooks-gemvbskfs0w.ws-eu77.gitpod.io/'
    

    def form_valid(self, form):
        form.instance.name = self.request.user.username
        book = get_object_or_404(Book, id=self.kwargs['pk'])
        form.instance.book = book
        form.save()
        
        return super().form_valid(form)


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user.username == comment.name:
        comment.delete()
        messages.warning(request, 'Your massege has been deleted!')
    
    if 'finance-book-list':
        return redirect('finance-book-list')
    elif 'biography-book-list':
        return redirect('biography-book-list')
    elif 'health-book-list':
        return redirect('health-book-list')
    elif 'spiritual-book-list':
        return redirect('spiritual-book-list')
    elif 'leadership-book-list':
        return redirect('leadership-book-list')
    else:
        return redirect('get_home_page')


class BookLike(View):

    def post(self, request, slug, *args, **kwargs):

        book = get_object_or_404(Book, slug=slug)
        if book.likes.filter(id=request.user.id).exists():
            book.likes.remove(request.user)
            messages.success(request,'You successfully disliked the book!')
        else:
            book.likes.add(request.user)
            messages.success(request, 'You successfully liked the book!')

        if 'finance-book-list':
            return redirect('finance-book-list')
        elif 'biography-book-list':
            return redirect('biography-book-list')
        elif 'health-book-list':
            return redirect('health-book-list')
        elif 'spiritual-book-list':
            return redirect('spiritual-book-list')
        elif 'leadership-book-list':
            return redirect('leadership-book-list')
        else:
            return redirect('get_home_page')


def edit_comment(request, comment_id):
    comment_edit = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form=CommentForm(request.POST, instance=comment_edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been successfully edited!')

        if 'finance-book-list':
            return redirect('finance-book-list')
        elif 'biography-book-list':
            return redirect('biography-book-list')
        elif 'health-book-list':
            return redirect('health-book-list')
        elif 'spiritual-book-list':
            return redirect('spiritual-book-list')
        elif 'leadership-book-list':
            return redirect('leadership-book-list')
        else:
            return redirect('get_home_page')


    form = CommentForm(instance=comment_edit)
    context = {
        'form': form
    }
    return render(request, 'edit_comment.html', context)
