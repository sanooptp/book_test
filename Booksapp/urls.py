from django.urls import include, path
from . import views

urlpatterns = [
    path("list_book/", views.BooksListView.as_view(), name='book_list'),
    path("add_book/", views.BooksAddView.as_view(), name = 'add_book'),
    path("view_one/<int:pk>/", views.ListOneBookView.as_view(), name = 'view_one'),
]