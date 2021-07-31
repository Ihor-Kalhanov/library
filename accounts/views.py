from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status

from accounts.models import User
from accounts.permissions import IsOwnerOrAdmin
from accounts.serializers import UserSerializer


class UserView(viewsets.ViewSet):
    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'update': [IsOwnerOrAdmin],
        'destroy': [IsOwnerOrAdmin],
    }

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(movie)
        return Response(serializer.data)

    def update(self, request, pk=None):
        book = User.objects.get(pk=pk)
        serializer = UserSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        book = User.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

