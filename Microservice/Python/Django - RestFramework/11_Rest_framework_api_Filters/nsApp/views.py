
from .models import Author,Book
from nsApp.serializers import AuthorSerializer,BookSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    filter_backends =  [DjangoFilterBackend]
    filterset_fields = ['firstName']

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer