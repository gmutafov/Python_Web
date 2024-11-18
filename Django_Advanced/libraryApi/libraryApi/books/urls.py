
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from libraryApi.books import views
from libraryApi.books.views import PublisherViewSet

router = DefaultRouter()
router.register('', PublisherViewSet)

urlpatterns = [
    path('books/', views.ListBooksView.as_view(), name='books-list'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book-viewset'),
    path('publisher-links/', views.PublisherHyperlinkView.as_view(), name='publisher-link'),
    path('publishers/', include(router.urls)),
]