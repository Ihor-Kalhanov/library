from rest_framework import viewsets
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import UserSerializer


class UserView(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
