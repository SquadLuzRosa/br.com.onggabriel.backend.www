from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CustomUserModelViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_staff=False, is_superuser=False)
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
