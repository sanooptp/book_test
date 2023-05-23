from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Books,Collection

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"

class CollectionSerializer(serializers.ModelSerializer):
    # image_url = serializers.ImageField(required=False)
    class Meta:
        model = Collection
        fields = ["book_one", "book_two", "image_url"]
    # def save(self, *args, **kwargs):
        # if self.instance.avatar:
        #     self.instance.avatar.delete()
        # return super().save(*args, **kwargs)