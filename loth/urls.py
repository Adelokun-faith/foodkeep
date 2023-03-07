from django.urls import path
from . import views

app_name = 'loth'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', views.MenuView.as_view(), name='menu'),
    path('', views.AboutView.as_view(), name='about'),
    path('', views.BooksView.as_view(), name='book'),
]