from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="users_post",
        description="Rota de criação de usuários",
        summary="Criar usuários",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="users_get_id",
        description="Rota de listagem de usuário",
        summary="Listar usuário",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(operation_id="users_put_id", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="users_patch_id",
        description="Rota de atualização de usuário",
        summary="Atualizar usuário",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="users_delete_id",
        description="Rota de deleção de usuário",
        summary="Deletar usuário",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
