import typing

from drf_yasg import utils
from django.utils.decorators import method_decorator
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from . import pagination
from .models import Recipe, Site


@method_decorator(name='list', decorator=utils.swagger_auto_schema(
    operation_summary="Get sites"
))
class SiteViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.SiteSerializer
    queryset = Site.objects.all()


@method_decorator(name='retrieve', decorator=utils.swagger_auto_schema(
    operation_summary="Get a recipe"
))
class RecipeViewSet(viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

    @utils.swagger_auto_schema(
        operation_summary='Query Recipes. Given an input query string return all the recipes that contain this '
                          'string in their names, categories or ingredients',
        operation_description='',
        query_serializer=serializers.QuerySerializer
    )
    @action(
        methods=['get'], detail=False, url_path='getRecipes',
        pagination_class=pagination.Pagination,
        serializer_class=serializers.RecipeSerializerShort,
    )
    def query_recipes(self, request):
        """Get recipes based on a query string
        :param request: The HTTP request.
        :return: The response.
        """
        query_params = serializers.QuerySerializer(data=self.request.query_params, context={'request': request})
        query_params.is_valid(raise_exception=True)
        data = query_params.validated_data
        site_ids = data['site_ids'][0]

        queryset = Recipe.objects.filter(Q(site_id__in=site_ids) & (
                Q(category__icontains=data['query']) |
                Q(name__icontains=data['query']) |
                Q(ingredients__description__icontains=data['query'])
        )).distinct()

        page = self.paginate_queryset(self.filter_queryset(queryset=queryset))
        serializer = serializers.RecipeSerializerShort(page, many=True)
        return Response(serializer.data)
