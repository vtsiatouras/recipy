from django.db import models


class AutoCreatedUpdatedModel(models.Model):
    """Helper abstract model for entities that track creation and update date at the database.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ingredient(AutoCreatedUpdatedModel):
    """Model for ingredients
    """
    description = models.TextField()

    class Meta:
        db_table = 'ingredients'


class Site(AutoCreatedUpdatedModel):
    """Model for sites
    """
    name = models.CharField(max_length=50)
    url = models.URLField()

    class Meta:
        db_table = 'sites'


class Recipe(AutoCreatedUpdatedModel):
    """Model for recipes
    """
    url = models.URLField()
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    instructions = models.TextField()
    image_url = models.URLField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='recipes_sites')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes_ingredients')

    class Meta:
        db_table = 'recipes'
