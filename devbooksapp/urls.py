from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_home_page, name='get_home_page'),
    path('finance/', views.FinanceBookList.as_view(), name='finance-book-list'),
]