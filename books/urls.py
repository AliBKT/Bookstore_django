from django.urls import path


from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name="book_list"),
    path('<int:pk>/', views.book_detail_view, name="book_deatail"),
    path('add/', views.book_create_view, name="add_book"),
    path('<int:pk>/update', views.BookUpdateView.as_view(), name="update_book"),
    path('<int:pk>/delete', views.BookDeleteView.as_view(), name="delete_book"),
]

