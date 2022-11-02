from django.urls import path


from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name="book_list"),
    path('<int:pk>/', views.BookDetailView.as_view(), name="book_deatail"),
    path('add/', views.BookCreateView.as_view(), name="add_book"),
]

