from xmlrpc.client import ResponseError

from django.core.serializers import serialize
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from libraryApi.books.models import Book
from libraryApi.books.serializers import BookSerializer


@api_view(['GET', 'POST'])
def list_books_view(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBooksView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBooksApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer