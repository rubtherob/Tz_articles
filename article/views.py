# Create your views here.
from rest_framework import permissions, status
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from article.models import Article
from article.serializers import ArticleSerializer

class Author(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.creator == request.user:
            return True
        return False


class ArticleView(ModelViewSet):
    queryset = Artcle.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,Author)

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = Article.objects.all()
        else:
            queryset = Article.objects.filter(Private=False)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)