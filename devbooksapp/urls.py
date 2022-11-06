from . import views
from django.urls import path
from devbooksapp.views import get_base_page

urlpatterns = [
    path('', get_base_page, name='get_base_page'),
]