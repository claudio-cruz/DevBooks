from django.shortcuts import render

def get_home_page(request):
    return render(request, 'index.html')

def get_finance_categorie_page(request):
    return render(request, 'finance.html')
