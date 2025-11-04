from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .filters import CustomUserFilterClass
from rest_framework import Response, status
from rest_framework.views import APIView


class CustomUserModelViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_staff=False, is_superuser=False)
    serializer_class = CustomUserSerializer
    rql_filter_class = CustomUserFilterClass
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateDefaultSuperuserView(APIView):
    """
    View perigosa para criar um superusuário padrão.
    DEVE SER REMOVIDA IMEDIATAMENTE APÓS O PRIMEIRO USO EM PRODUÇÃO.
    """
    permission_classes = []

    def post(self, request):
        username = 'daniel'
        email = 'daniel@gmail.com'
        password = 'erick292120'

        if CustomUser.objects.filter(username=username).exists():
            return Response(
                {"detail": f"Superusuário '{username}' já existe. Usuário não foi criado."},
                status=status.HTTP_409_CONFLICT
            )

        try:
            # 3. Criar o superusuário usando o método recomendado
            CustomUser.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            return Response(
                {"detail": f"Superusuário '{username}' criado com sucesso! REMOVA ESTA ROTA IMEDIATAMENTE."},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"detail": f"Erro ao criar superusuário: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
