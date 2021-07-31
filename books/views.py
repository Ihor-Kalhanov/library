from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404
from books.models import Book
from books.permissions import IsOwnerOrAdminOrReadOnly
from books.serializers import Bookserializer
from rest_framework.response import Response
from rest_framework import status


class BooksView(viewsets.ViewSet):
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [IsAuthenticated],
                                    'retrieve': [IsAuthenticated],
                                    'update': [IsOwnerOrAdminOrReadOnly],
                                    'destroy': [IsOwnerOrAdminOrReadOnly],
                                    }


    def list(self, request):
        queryset = Book.objects.all()
        serializer = Bookserializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = Bookserializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = Bookserializer(movie)
        return Response(serializer.data)

    def update(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        serializer = Bookserializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]





