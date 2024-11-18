from django import forms
from rest_framework import serializers

from libraryApi.books.models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        authors = validated_data.pop('author')
        author_names = [a['name'] for a in authors]

        book = Book.objects.create(**validated_data)

        existing_authors = Author.objects.filter(name__in=author_names)
        existing_authors_names = set(existing_authors.values_list('name', flat=True))
        new_authors_names = set(author_names) - existing_authors_names

        new_authors = [Author(name=a_name) for a_name in new_authors_names]

        created_authors = Author.objects.bulk_create(new_authors)
        all_authors = list(existing_authors) + list(created_authors)
        book.author.set(all_authors)

        return book


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class PublisherHyperLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

