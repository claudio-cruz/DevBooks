from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book, Category
from .forms import CommentForm


def get_home_page(request):
    return render(request, 'index.html')

class FinanceBookList(generic.ListView):
    model = Book
    template_name = "finance.html"
    paginate_by = 10

    def get_queryset(self):
            filter_list= Book.objects.filter(category= 34).filter(status= 1)
            return filter_list
    