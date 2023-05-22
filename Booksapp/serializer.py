from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"
