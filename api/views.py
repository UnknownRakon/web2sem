from rest_framework import viewsets

from api.seriallizers import UserSerializer

from .models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
