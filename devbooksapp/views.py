from django.shortcuts import render

def get_base_page(request):
    return render(request, 'index.html')
