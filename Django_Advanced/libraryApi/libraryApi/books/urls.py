from django.urls import path

from libraryApi.books import views

urlpatterns = [
    path('books/', views.ListBooksApiView.as_view(), name='books'),
]