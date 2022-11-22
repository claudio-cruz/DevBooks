from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_home_page, name='get_home_page'),
    path('finance/', views.FinanceBookList.as_view(), name='finance-book-list'),
    path('biography/', views.BiographyBookList.as_view(), name='biography-book-list'),
    path('health/', views.HealthBookList.as_view(), name='health-book-list'),
    path('spiritual/', views.SpiritualBookList.as_view(), name='spiritual-book-list'),
    path('leadership/', views.LeadershipBookList.as_view(), name='leadership-book-list'),
]