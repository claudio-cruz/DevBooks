from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('finance/', views.FinanceBookList.as_view(), name='finance-book-list'),
    path('biography/', views.BiographyBookList.as_view(), name='biography-book-list'),
    path('health/', views.HealthBookList.as_view(), name='health-book-list'),
    path('spiritual/', views.SpiritualBookList.as_view(), name='spiritual-book-list'),
    path('leadership/', views.LeadershipBookList.as_view(), name='leadership-book-list'),
    path('aboutus/', views.AboutUsPage.as_view(), name='get_aboutus_page'),
    path('comment/<int:pk>', views.CommentBookList.as_view(), name="comment"),
    path('delete/<comment_id>', views.delete_comment, name='delete'),
    path('edit/<comment_id>', views.edit_comment, name='edit-comment'),
    path('like/<slug:slug>', views.BookLike.as_view(), name='book_like'),
]