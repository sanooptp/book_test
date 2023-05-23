from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, permissions, views, status
from .models import Books, Collection
from .serializer import BooksSerializer, CollectionSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import json

class BooksListView(generics.ListAPIView):
    queryset = Books.objects.filter(pk=1)
    serializer_class = BooksSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        queryset = self.get_queryset()
        user = request.user.username
        serializer = BooksSerializer(queryset, many=True)
        data= {"status": "Success", "user": user, "data": serializer.data}
        return Response(data)


class BooksAddView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # content = body['new_name']
        queryset = self.get_queryset()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            return Response(data["new_name"])


class ListOneBookView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        queryset = self.get_queryset()
        user = User.objects.filter(pk=pk)
        return Response(user[0].username)


class CollectionView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.data['image_url']
        image = Collection.objects.create(image_url=file)
        return Response(json.dumps({'message': "Uploaded"}), status=200)

    # def post(self, request, format=None):
    #     serializer = CollectionSerializer(data=request.data, instance=request.user)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)