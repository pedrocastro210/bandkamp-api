from rest_framework.views import APIView, status, Response
from .models import Album
from .serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class AlbumView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @extend_schema(
        operation_id="albums_get",
        description="Rota de listagem de álbuns",
        summary="Listar álbuns",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="albums_post",
        description="Rota de criação de álbuns",
        summary="Criar álbums",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
