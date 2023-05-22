from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, permissions
from .models import Books
from .serializer import BooksSerializer

class BooksListView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]


class BooksAddView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListOneBookView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]

