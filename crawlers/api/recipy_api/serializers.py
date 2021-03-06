from rest_framework.serializers import ModelSerializer, Serializer, CharField, ListField, ValidationError

from .models import Recipe, Site, Ingredient


class BaseSerializer(Serializer):
    """Base serializer that adds default implementation for the create and update methods that do nothing. Serializers
    that do not need those methods can extend this class.
    """

    def create(self, validated_data):
        """Not implemented
        """
        pass

    def update(self, instance, validated_data):
        """Not implemented
        """
        pass


class SiteSerializer(ModelSerializer):
    """Site serializer
    """

    class Meta:
        model = Site
        fields = ['id', 'url', 'name']


class IngredientSerializer(ModelSerializer):
    """Ingredient serializer
    """

    class Meta:
        model = Ingredient
        fields = ['id', 'description']


class RecipeSerializer(ModelSerializer):
    """Recipe serializer
    """
    site = SiteSerializer()
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'url', 'name', 'category', 'instructions', 'image_url', 'site', 'ingredients']


class RecipeSerializerShort(ModelSerializer):
    """Recipe serializer short details
    """
    site = SiteSerializer()

    class Meta:
        model = Recipe
        fields = ['id', 'url', 'name', 'category', 'image_url', 'site']


class QuerySerializer(BaseSerializer):
    """Serializer used for querying recipes
    """
    query = CharField(help_text='The query string to search recipes', required=True)
    site_ids = ListField(help_text='Site IDs separated with comma', required=False)

    def to_internal_value(self, data):
        data._mutable = True
        site_ids_data = data['site_ids']
        try:
            data['site_ids'] = [int(site_id) for site_id in site_ids_data.split(',')]
            data._mutable = False
            return super(QuerySerializer, self).to_internal_value(data)
        except (TypeError, ValueError):
            raise ValidationError({data['site_ids']: 'incorrect_type'})
